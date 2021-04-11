from scipy.stats import truncnorm

import numpy as np
import gym
from reward_machines.rm_environment import RewardMachineEnv

class VC_Env(gym.Env):
    def __init__(self, time_limit, std=0.2):
        self.state = np.array([5.0, 0.]) + truncnorm.rvs(-1, 1, 0, 0.3, 2)
        self.time_limit = time_limit
        self.time = 0
        self.std = std
        self.observation_space = gym.spaces.Box(-np.inf, np.inf, shape=(2,))
        self.action_space = gym.spaces.Box(-1, 1, shape=(2,))
        
    def reset(self):
        self.state = np.array([5.0, 0.]) + truncnorm.rvs(-1, 1, 0, 0.3, 2)
        self.time = 0
        return self.state

    def step(self, action):
        action = action * np.array([0.5, np.pi]) + np.array([0.5, 0.])
        velocity = action[0] * np.array([np.cos(action[1]), np.sin(action[1])])
        next_state = self.state + velocity + truncnorm.rvs(-1, 1, 0, self.std, 2)
        self.state = next_state
        self.time = self.time + 1
        #return next_state, 0, self.time > self.time_limit, None
        #### adjust
        return next_state, 0, self.time > self.time_limit, {}

    def render(self):
        pass

    def get_sim_state(self):
        return self.state

    def set_sim_state(self, state):
        self.state = state
        return self.state

    def close(self):
        pass

    #    obstacle: np.array(4): [x_min, y_min, x_max, y_max]
    def is_collision(self, obstacle):
        sys_state = self.state
        temp_val = max([obstacle[0] - sys_state[0],
                        obstacle[1] - sys_state[1],
                        sys_state[0] - obstacle[2],
                        sys_state[1] - obstacle[3]])
        if temp_val > 0:
            return False
        return True
    
    #    goal: np.array(2), err: float
    def reach(self, goal, err):
        sys_state = self.state
        
        temp_val = min([sys_state[0] - goal[0],
                        goal[0] - sys_state[0],
                        sys_state[1] - goal[1],
                        goal[1] - sys_state[1]]) + err
        if temp_val < 0:
            return False
        return True

    def get_events(self):
        #Obstacle
        obs = np.array([4.0, 4.0, 6.0, 6.0])
        
        #Goal positions
        gt1 = np.array([3.0, 4.0])
        gt2 = np.array([6.0, 0.0])
        gfinal = np.array([3.0, 7.0])
        
        events = ''
        if self.is_collision(obs):
            events+='c'
        if self.reach(gt1, 0.5):
            events+='a'
        if self.reach(gt2, 0.5):
            events+='b'
        if self.reach(gfinal, 0.5):
            events+='f'
        return events
    
class MyVC_EnvRM1(RewardMachineEnv):
    def __init__(self):
        env = VC_Env(500, std=0.05)
        rm_files = ["./envs/car2d/reward_machines/rm1.txt"]
        super().__init__(env, rm_files)

