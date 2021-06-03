
from reward_machines.rm_environment import RewardMachineEnv
from reward_machines.reward_machine import RewardMachine
from reward_machines.reward_functions import RoomRewardFunction, ConstantRewardFunction, RoomRewardFunctionObstacle

from envs.rooms.rooms import GridParams, RoomsEnv, AbstractState
from envs.rooms.rooms_envs import GRID_PARAMS_LIST, MAX_TIMESTEPS, START_ROOM, FINAL_ROOM

class nine_rooms_back_and_forth(RewardMachineEnv):
    def __init__(self):
        env_num = 2
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])
        
        rm = RewardMachine("./envs/rooms/reward_machines/m1.txt")

        loop_goal = [[(2,0)], [(0,0)]]
        for i in range(len(loop_goal)):
            goal_list = loop_goal[i]
            center_list = [grid_params.get_center_region(room).region for room in goal_list]
            rm.delta_r[i][i] = RoomRewardFunction(center_list)
                
        super().__init__(env, rm)

class nine_rooms_half_continuous(RewardMachineEnv):
    def __init__(self):
        env_num = 2
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])
        
        rm = RewardMachine("./envs/rooms/reward_machines/m2.txt")

        goal_list = [(2,0), (0,2)]
        center_list = [grid_params.get_center_region(room).region for room in goal_list]
        
        rm.delta_r[0][0] = RoomRewardFunction(center_list)
        
        super().__init__(env, rm)

class nine_rooms_one_continuous(RewardMachineEnv):
    def __init__(self):
        env_num = 2
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])
        
        rm = RewardMachine("./envs/rooms/reward_machines/m3.txt")

        loop_goal = [[(2,0), (0,2)], [2,2], [2,2]]
        for i in range(len(loop_goal)):
            goal_list = loop_goal[i]
            center_list = [grid_params.get_center_region(room).region for room in goal_list]
            rm.delta_r[i][i] = RoomRewardFunction(center_list)

        super().__init__(env, rm)

class nine_rooms_obstacle_continuous(RewardMachineEnv):
    def __init__(self):
        env_num = 2
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])
        
        rm = RewardMachine("./envs/rooms/reward_machines/m4.txt")

        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region

        goal = (2,0)
        center_list = [grid_params.get_center_region(goal).region]
        rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)

        super().__init__(env, rm)

class nine_rooms_one_obstacle_continuous(RewardMachineEnv):
    def __init__(self):
        env_num = 2
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])
        
        rm = RewardMachine("./envs/rooms/reward_machines/m5.txt")

        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region

        loop_goal = [[(2,0), (0,2)], [2,2], [2,2]]
        for i in range(len(loop_goal)):
            goal_list = loop_goal[i]
            center_list = [grid_params.get_center_region(room).region for room in goal_list]
        
            if i==0:
                rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)
            else:
                rm.delta_r[i][i] = RoomRewardFunction(center_list)

        super().__init__(env, rm)



class sixteen_rooms_half_continuous(RewardMachineEnv):
    def __init__(self):
        env_num = 3
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])

        rm = RewardMachine("./envs/rooms/reward_machines/rm1.txt")

        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region
        goal_list = [(2,0), (0,2)]
        center_list = [grid_params.get_center_region(room).region for room in goal_list]
        rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)
    
        super().__init__(env, rm)

class sixteen_rooms_one_continuous(RewardMachineEnv):
    def __init__(self):
        env_num = 3
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])

        rm = RewardMachine("./envs/rooms/reward_machines/rm2.txt")

        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region

        loop_goal = [[(2,0), (0,2)], [(2,2)], [(2,2)]]
        for i in range(len(loop_goal)):
            goal_list = loop_goal[i]
            center_list = [grid_params.get_center_region(room).region for room in goal_list]
            if i==0:
                rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)
            else:
                rm.delta_r[i][i] = RoomRewardFunction(center_list)
        

        super().__init__(env, rm)

class sixteen_rooms_two_continuous(RewardMachineEnv):
    def __init__(self):
        env_num = 3
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])

        rm = RewardMachine("./envs/rooms/reward_machines/rm3.txt")
        
        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region

        loop_goal = [[(2,0), (0,2)], [(2,2)], [(2,2)], [(2,1), (3,2)], [(3,1)], [(3,1)]]
        for i in range(len(loop_goal)):
            goal_list = loop_goal[i]
            center_list = [grid_params.get_center_region(room).region for room in goal_list]
            if i==0:
                rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)
            else:
                rm.delta_r[i][i] = RoomRewardFunction(center_list)
        
        super().__init__(env, rm)

class sixteen_rooms_three_continuous(RewardMachineEnv):
    def __init__(self):
        env_num = 3
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])

        rm = RewardMachine("./envs/rooms/reward_machines/rm4.txt")
        
        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region

        obstacle2 = (2,3)
        obstacle_list2 = grid_params.get_center_region(obstacle2).region
        
        loop_goal = [[(2,0), (0,2)],
                     [(2,2)],
                     [(2,2)],
                     [(2,1), (3,2)],
                     [(3,1)],
                     [(3,1)],
                     [(1,1), (3,3)],
                     [(1,3)],
                     [(1,3)]]
     
        for i in range(len(loop_goal)):
            goal_list = loop_goal[i]
            center_list = [grid_params.get_center_region(room).region for room in goal_list]
            if i==0:
                rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)
            if goal_list == [(1,3)]:
                rm.delta_r[i][i] = RoomRewardFunctionObstacle(center_list, obstacle_list2)
            
            else:
                rm.delta_r[i][i] = RoomRewardFunction(center_list)
        
        super().__init__(env, rm)

class sixteen_rooms_four_continuous(RewardMachineEnv):
    def __init__(self):
        env_num = 3
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])

        rm = RewardMachine("./envs/rooms/reward_machines/rm5.txt")
        
        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region

        obstacle2 = (2,3)
        obstacle_list2 = grid_params.get_center_region(obstacle2).region
        
        loop_goal = [[(2,0), (0,2)],
                     [(2,2)],
                     [(2,2)],
                     [(2,1), (3,2)],
                     [(3,1)],
                     [(3,1)],
                     [(1,1), (3,3)],
                     [(1,3)],
                     [(1,3)],
                     [(1,1),(0,3)],
                     [(0,1)],
                     [(0,1)]]
     
        for i in range(len(loop_goal)):
            goal_list = loop_goal[i]
            center_list = [grid_params.get_center_region(room).region for room in goal_list]
            if i==0:
                rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)
            if goal_list == [(1,3)]:
                rm.delta_r[i][i] = RoomRewardFunctionObstacle(center_list, obstacle_list2)   
            else:
                rm.delta_r[i][i] = RoomRewardFunction(center_list)
        
        super().__init__(env, rm)

class sixteen_rooms_half_continuous_more_doors(RewardMachineEnv):
    def __init__(self):
        env_num = 4
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])

        rm = RewardMachine("./envs/rooms/reward_machines/rm1.txt")

        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region
        goal_list = [(2,0), (0,2)]
        center_list = [grid_params.get_center_region(room).region for room in goal_list]
        rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)
    
        super().__init__(env, rm)

class sixteen_rooms_one_continuous_more_doors(RewardMachineEnv):
    def __init__(self):
        env_num = 4
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])

        rm = RewardMachine("./envs/rooms/reward_machines/rm2.txt")

        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region

        loop_goal = [[(2,0), (0,2)], [(2,2)], [(2,2)]]
        for i in range(len(loop_goal)):
            goal_list = loop_goal[i]
            center_list = [grid_params.get_center_region(room).region for room in goal_list]
            if i==0:
                rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)
            else:
                rm.delta_r[i][i] = RoomRewardFunction(center_list)
        

        super().__init__(env, rm)

class sixteen_rooms_two_continuous_more_doors(RewardMachineEnv):
    def __init__(self):
        env_num = 4
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])

        rm = RewardMachine("./envs/rooms/reward_machines/rm3.txt")
        
        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region

        loop_goal = [[(2,0), (0,2)], [(2,2)], [(2,2)], [(2,1), (3,2)], [(3,1)], [(3,1)]]
        for i in range(len(loop_goal)):
            goal_list = loop_goal[i]
            center_list = [grid_params.get_center_region(room).region for room in goal_list]
            if i==0:
                rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)
            else:
                rm.delta_r[i][i] = RoomRewardFunction(center_list)
        
        super().__init__(env, rm)

class sixteen_rooms_three_continuous_more_doors(RewardMachineEnv):
    def __init__(self):
        env_num = 4
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])

        rm = RewardMachine("./envs/rooms/reward_machines/rm4.txt")
        
        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region

        obstacle2 = (2,3)
        obstacle_list2 = grid_params.get_center_region(obstacle2).region
        
        loop_goal = [[(2,0), (0,2)],
                     [(2,2)],
                     [(2,2)],
                     [(2,1), (3,2)],
                     [(3,1)],
                     [(3,1)],
                     [(1,1), (3,3)],
                     [(1,3)],
                     [(1,3)]]
     
        for i in range(len(loop_goal)):
            goal_list = loop_goal[i]
            center_list = [grid_params.get_center_region(room).region for room in goal_list]
            if i==0:
                rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)
            if goal_list == [(1,3)]:
                rm.delta_r[i][i] = RoomRewardFunctionObstacle(center_list, obstacle_list2)
            
            else:
                rm.delta_r[i][i] = RoomRewardFunction(center_list)
        
        super().__init__(env, rm)

class sixteen_rooms_four_continuous_more_doors(RewardMachineEnv):
    def __init__(self):
        env_num = 4
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])

        rm = RewardMachine("./envs/rooms/reward_machines/rm5.txt")
        
        obstacle = (1,0)
        obstacle_list = grid_params.get_center_region(obstacle).region

        obstacle2 = (2,3)
        obstacle_list2 = grid_params.get_center_region(obstacle2).region
        
        loop_goal = [[(2,0), (0,2)],
                     [(2,2)],
                     [(2,2)],
                     [(2,1), (3,2)],
                     [(3,1)],
                     [(3,1)],
                     [(1,1), (3,3)],
                     [(1,3)],
                     [(1,3)],
                     [(1,1),(0,3)],
                     [(0,1)],
                     [(0,1)]]
     
        for i in range(len(loop_goal)):
            goal_list = loop_goal[i]
            center_list = [grid_params.get_center_region(room).region for room in goal_list]
            if i==0:
                rm.delta_r[0][0] = RoomRewardFunctionObstacle(center_list, obstacle_list)
            if goal_list == [(1,3)]:
                rm.delta_r[i][i] = RoomRewardFunctionObstacle(center_list, obstacle_list2)   
            else:
                rm.delta_r[i][i] = RoomRewardFunction(center_list)
        
        super().__init__(env, rm)

        
class nine_rooms_half(RewardMachineEnv):
    def __init__(self):
        env_num = 2
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])

        rm = RewardMachine("./envs/rooms/reward_machines/rm1.txt")
        super().__init__(env, rm)

class nine_rooms_one(RewardMachineEnv):
    def __init__(self):
        env_num = 2
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])
        rm_files = ["./envs/rooms/reward_machines/rm2.txt"]
        super().__init__(env, rm_files)


class sixteen_rooms_half(RewardMachineEnv):
    def __init__(self):
        env_num = 3
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])
        rm_files = ["./envs/rooms/reward_machines/rm1.txt"]
        super().__init__(env, rm_files)

class sixteen_rooms_one(RewardMachineEnv):
    def __init__(self):
        env_num = 3
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])
        rm_files = ["./envs/rooms/reward_machines/rm2.txt"]
        super().__init__(env, rm_files)

class sixteen_rooms_two(RewardMachineEnv):
    def __init__(self):
        env_num = 3
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])
        rm_files = ["./envs/rooms/reward_machines/rm3.txt"]
        super().__init__(env, rm_files)


