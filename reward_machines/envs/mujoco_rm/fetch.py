import os
import mujoco_py

import gym
from gym import utils
from gym.envs.robotics import fetch_env
from copy import deepcopy

#For get_label
from numpy import linalg as LA
import numpy as np


from reward_machines.rm_environment import RewardMachineEnv
#from reward_machines.reward_machine import RewardMachine
#from reward_machines.reward_functions import ConstantRewardFunction


# Ensure we get the path separator correct on windows
PICK_MODEL_XML_PATH = os.path.join('fetch', 'pick_and_place.xml')
REACH_MODEL_XML_PATH = os.path.join('fetch', 'reach.xml')
PUSH_MODEL_XML_PATH = os.path.join('fetch', 'push.xml')


class FetchEnvWithStates(fetch_env.FetchEnv):

    def get_sim_state(self):
        return deepcopy(self.sim.get_state())

    def set_sim_state(self, state):
        self.sim.reset()
        old_state = self.sim.get_state()
        new_state = mujoco_py.MjSimState(old_state.time, state.qpos, state.qvel,
                                         state.act, state.udd_state)
        self.sim.set_state(new_state)
        self.sim.forward()
        return self._get_obs()

    def my_get_obs():
        return self._get_obs()

class FetchPickAndPlaceEnv(FetchEnvWithStates, utils.EzPickle):
    def __init__(self, reward_type='sparse'):
        initial_qpos = {
            'robot0:slide0': 0.405,
            'robot0:slide1': 0.48,
            'robot0:slide2': 0.0,
            'object0:joint': [1.25, 0.53, 0.4, 1., 0., 0., 0.],
        }
        fetch_env.FetchEnv.__init__(
            self, PICK_MODEL_XML_PATH, has_object=True, block_gripper=False, n_substeps=20,
            gripper_extra_height=0.2, target_in_the_air=True, target_offset=0.0,
            obj_range=0.15, target_range=0.15, distance_threshold=0.05,
            initial_qpos=initial_qpos, reward_type=reward_type)
        utils.EzPickle.__init__(self)


class FetchReachEnv(FetchEnvWithStates, utils.EzPickle):
    def __init__(self, reward_type='sparse'):
        initial_qpos = {
            'robot0:slide0': 0.4049,
            'robot0:slide1': 0.48,
            'robot0:slide2': 0.0,
        }
        fetch_env.FetchEnv.__init__(
            self, REACH_MODEL_XML_PATH, has_object=False, block_gripper=True, n_substeps=20,
            gripper_extra_height=0.2, target_in_the_air=True, target_offset=0.0,
            obj_range=0.15, target_range=0.15, distance_threshold=0.05,
            initial_qpos=initial_qpos, reward_type=reward_type)
        utils.EzPickle.__init__(self)


class FetchPushEnv(FetchEnvWithStates, utils.EzPickle):
    def __init__(self, reward_type='sparse'):
        initial_qpos = {
            'robot0:slide0': 0.405,
            'robot0:slide1': 0.48,
            'robot0:slide2': 0.0,
            'object0:joint': [1.25, 0.53, 0.4, 1., 0., 0., 0.],
        }
        fetch_env.FetchEnv.__init__(
            self, PUSH_MODEL_XML_PATH, has_object=True, block_gripper=True, n_substeps=20,
            gripper_extra_height=0.0, target_in_the_air=False, target_offset=0.0,
            obj_range=0.15, target_range=0.15, distance_threshold=0.05,
            initial_qpos=initial_qpos, reward_type=reward_type)
        utils.EzPickle.__init__(self)


class ObservationWrapper(gym.Env):
    '''
    Wraps an environment modifying dictionary obervations into array observations.
    '''

    def __init__(self, env, keys, relative=None, max_timesteps=10000):
        self.env = env
        self.keys = keys
        self.relative = relative
        self.max_timesteps = max_timesteps

        obs = self.env.reset()
        obs_dim = sum([obs[key].shape[0] for key in self.keys])
        if self.relative is not None:
            obs_dim += relative[0][2] - relative[0][1]
        self.action_space = self.env.action_space
        self.observation_space = gym.spaces.Box(-np.inf, np.inf, shape=(obs_dim,))

    def reset(self):
        self.t = 0
        obs = self.env.reset()
        return self.flatten_obs(obs)

    def step(self, action):
        #print(action)
        obs, rew, done, info = self.env.step(action)
        info['my_cur_pos'] = self.flatten_obs(obs)
        self.t += 1
        done = done or self.t > self.max_timesteps
        return self.flatten_obs(obs), rew, done, info

    def render(self):
        return self.env.render()

    def get_sim_state(self):
        return self.env.get_sim_state()

    def set_sim_state(self, state):
        return self.flatten_obs(self.env.set_sim_state(state))

    def close(self):
        self.env.close()

    def flatten_obs(self, obs):
        flat_obs = np.concatenate([obs[key] for key in self.keys])
        if self.relative is not None:
            (key1, i1, j1) = self.relative[0]
            (key2, i2, j2) = self.relative[1]
            rel_obs = obs[key1][i1:j1] - obs[key2][i2:j2]
            flat_obs = np.concatenate([flat_obs, rel_obs])
        return flat_obs

    def get_events(self):
        label = ''
        sys_state = self.flatten_obs(self.env._get_obs())

        err1 = 0.03
        err2 = 0.05
        
        #grip near object
        dist = sys_state[:3] - (sys_state[3:6] + np.array([0., 0., 0.065]))
        dist = np.concatenate([dist, [sys_state[9] + sys_state[10] - 0.1]])
        if (-LA.norm(dist) + err1)>0:
            label += 'n'

        # hold object
        dist = sys_state[:3] - sys_state[3:6]
        dist2 = np.concatenate([dist, [sys_state[9] + sys_state[10] - 0.045]])
        if (-LA.norm(dist2) + err1)>0:
            label += 'h'

        # Object in air
        if (sys_state[5] - 0.45)>0:
            label+= 'a'
        

        # object at goal
        dist = np.concatenate([sys_state[-3:], [sys_state[9] + sys_state[10] - 0.045]])
        if (-LA.norm(dist) + err2)>0:
            label += 'g'

        # object at fixed goal
        goal = np.array([1.15, 1.0, 0.5])
        if (-LA.norm(sys_state[3:6] - goal) + err2)>0:
            label += 'f'

        goal = np.array([1.45, 1.0, 0.5])
        if (-LA.norm(sys_state[3:6] - goal) + err2)>0:
            label += 'h'

        goal = np.array([1.15, 1.0, 0.425])
        if (-LA.norm(sys_state[3:6] - goal) + err2)>0:
            label += 'l'

        goal = np.array([1.50, 1.05, 0.425])
        if (-LA.norm(sys_state[3:6] - goal) + 0.01)>0:
            label += 'm'

        return label

class fpp_goal(RewardMachineEnv):
    def __init__(self):
        env = ObservationWrapper(FetchPickAndPlaceEnv(), ['observation', 'desired_goal'],
                                 relative=(('desired_goal', 0, 3), ('observation', 3, 6)))

        rm_files = ["./envs/mujoco_rm/reward_machines/rm1.txt"]
        super().__init__(env, rm_files)

class fpp_fixed_goal(RewardMachineEnv):
    def __init__(self):
        env = ObservationWrapper(FetchPickAndPlaceEnv(), ['observation', 'desired_goal'],
                                 relative=(('desired_goal', 0, 3), ('observation', 3, 6)))

        rm_files = ["./envs/mujoco_rm/reward_machines/rm2.txt"]
        super().__init__(env, rm_files)

class fpp_fixed_goal_choice(RewardMachineEnv):
    def __init__(self):
        env = ObservationWrapper(FetchPickAndPlaceEnv(), ['observation', 'desired_goal'],
                                 relative=(('desired_goal', 0, 3), ('observation', 3, 6)))

        rm_files = ["./envs/mujoco_rm/reward_machines/rm3.txt"]
        super().__init__(env, rm_files)

    
