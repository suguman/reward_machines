import math
import numpy as np

from numpy import linalg as LA

class RewardFunction:
    def __init__(self):
        pass

    # To implement...
    def get_reward(self, s_info):
        raise NotImplementedError("To be implemented")

    def get_type(self):
        raise NotImplementedError("To be implemented")


class ConstantRewardFunction(RewardFunction):
    """
    Defines a constant reward for a 'simple reward machine'
    """
    def __init__(self, c):
        super().__init__()
        self.c = c

    def get_type(self):
        return "constant"

    def get_reward(self, s_info):
        return self.c

class RewardControl(RewardFunction):
    """
    Gives a reward for moving forward
    """
    def __init__(self):
        super().__init__()

    def get_type(self):
        return "ctrl"

    def get_reward(self, s_info):
        return s_info['reward_ctrl']

class RewardForward(RewardFunction):
    """
    Gives a reward for moving forward
    """
    def __init__(self):
        super().__init__()

    def get_type(self):
        return "forward"

    def get_reward(self, s_info):
        return s_info['reward_run'] + s_info['reward_ctrl']  #Cheetah


class RewardBackwards(RewardFunction):
    """
    Gives a reward for moving backwards
    """
    def __init__(self):
        super().__init__()

    def get_type(self):
        return "backwards"

    def get_reward(self, s_info):
        return -s_info['reward_run'] + s_info['reward_ctrl']  #Cheetah


class RoomRewardFunction(RewardFunction):
    
    def __init__(self, goallist):
        super().__init__()
        self.goallist = goallist

    def get_type(self):
        return "Rooms-Continuous"

    def get_reward(self, s_info):
    
        sys_state = s_info['cur_pos']

        reward = -10000
        for elem in self.goallist:
            #print(elem, elem[0], elem[1])
            low = elem[0]
            high = elem[1]
            temp = min(np.concatenate([sys_state[:2] - low, high - sys_state[:2]]))
            reward = max(temp, reward)
            
        return reward  # Rooms: Continuous

class RoomRewardFunctionObstacle(RewardFunction):
    
    def __init__(self, goallist, obstacle):
        super().__init__()
        self.goallist = goallist
        self.obstacle = obstacle

    def get_type(self):
        return "Rooms-with-Obstacle-Continuous"

    def get_reward(self, s_info):
    
        sys_state = s_info['cur_pos']

        reward = -10000
        for elem in self.goallist:
            #print(elem, elem[0], elem[1])
            low = elem[0]
            high = elem[1]
            temp = min(np.concatenate([sys_state[:2] - low, high - sys_state[:2]]))
            reward = max(temp, reward)

        obs_low = self.obstacle[0]
        obs_high = self.obstacle[1]
        reward_obs = 10*max(np.concatenate(low - [sys_state[:2], sys_state[:2] - high]))

        total_reward = reward + min(reward_obs, 0)
            
        return total_reward  # Rooms: Continuous


class FetchNearObjectReward(RewardFunction):

    def __init__(self):
        super().__init__()

    def get_type(self):
        return "Fetch-GripNearObject"

    def get_reward(self, s_info):
        err = 0.03
        
        sys_state = s_info['my_cur_pos']
        dist = sys_state[:3] - (sys_state[3:6] + np.array([0., 0., 0.065]))
        dist = np.concatenate([dist, [sys_state[9] + sys_state[10] - 0.1]])

        return -LA.norm(dist) + err

class FetchHoldObjectReward(RewardFunction):

    def __init__(self):
        super().__init__()

    def get_type(self):
        return "Fetch-HoldObject"

    def get_reward(self, s_info):
        err = 0.03
        
        sys_state = s_info['my_cur_pos']
        dist = sys_state[:3] - sys_state[3:6] 
        dist2 = np.concatenate([dist, [sys_state[9] + sys_state[10] - 0.1]])

        return -LA.norm(dist2) + err


class FetchObjectInAirReward(RewardFunction):

    def __init__(self):
        super().__init__()

    def get_type(self):
        return "Fetch-ObjectInAir"

    def get_reward(self, s_info):
        sys_state = s_info['my_cur_pos']
        return sys_state[5] - 0.45


class FetchObjectAtGoalReward(RewardFunction):

    def __init__(self):
        super().__init__()

    def get_type(self):
        return "Fetch-ObjectAtGoal"

    def get_reward(self, s_info):
        err = 0.05
        sys_state = s_info['my_cur_pos']
        dist = np.concatenate([sys_state[-3:], [sys_state[9] + sys_state[10] - 0.045]])
        return -LA.norm(dist) + err

class FetchObjectAtGoalFixedReward(RewardFunction):

    def __init__(self, goalposlist):
        super().__init__()
        
        self.goalposlist = goalposlist

    def get_type(self):
        return "Fetch-ObjectAtGoalFixed"

    def get_reward(self, s_info):
        
        sys_state = s_info['my_cur_pos']

        reward = -10000
        for goalpos in self.goalposlist:
            if goalpos == [1.50, 1.05, 0.425]:
                err = 0.01
            else:
                err = 0.05
            goal = np.array(goalpos)
            reward = max(reward, -LA.norm(sys_state[3:6] - goal) + err)

        return reward

    

    

    
