
from reward_machines.rm_environment import RewardMachineEnv

from envs.rooms.rooms import GridParams, RoomsEnv

from envs.rooms.rooms_envs import GRID_PARAMS_LIST, MAX_TIMESTEPS, START_ROOM, FINAL_ROOM


        
class nine_rooms_half(RewardMachineEnv):
    def __init__(self):
        env_num = 2
        grid_params = GRID_PARAMS_LIST[env_num]
        env = RoomsEnv(grid_params, START_ROOM[env_num], FINAL_ROOM[env_num])
        rm_files = ["./envs/rooms/reward_machines/rm1.txt"]
        super().__init__(env, rm_files)

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

