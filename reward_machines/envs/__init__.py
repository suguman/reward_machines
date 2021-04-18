from gym.envs.registration import register

# ----------------------------------------- Half-Cheetah

register(
    id='Half-Cheetah-RM1-v0',
    entry_point='envs.mujoco_rm.half_cheetah_environment:MyHalfCheetahEnvRM1',
    max_episode_steps=1000,
)
register(
    id='Half-Cheetah-RM2-v0',
    entry_point='envs.mujoco_rm.half_cheetah_environment:MyHalfCheetahEnvRM2',
    max_episode_steps=1000,
)



# ----------------------------------------- WATER
for i in range(11):
    w_id = 'Water-M%d-v0'%i
    w_en = 'envs.water.water_environment:WaterRMEnvM%d'%i
    register(
        id=w_id,
        entry_point=w_en,
        max_episode_steps=600
    )

for i in range(11):
    w_id = 'Water-single-M%d-v0'%i
    w_en = 'envs.water.water_environment:WaterRM10EnvM%d'%i
    register(
        id=w_id,
        entry_point=w_en,
        max_episode_steps=600
    )

# ----------------------------------------- OFFICE
register(
    id='Office-v0',
    entry_point='envs.grids.grid_environment:OfficeRMEnv',
    max_episode_steps=1000
)

register(
    id='Office-single-v0',
    entry_point='envs.grids.grid_environment:OfficeRM3Env',
    max_episode_steps=1000
)

# ----------------------------------------- CRAFT
for i in range(11):
    w_id = 'Craft-M%d-v0'%i
    w_en = 'envs.grids.grid_environment:CraftRMEnvM%d'%i
    register(
        id=w_id,
        entry_point=w_en,
        max_episode_steps=1000
    )

for i in range(11):
    w_id = 'Craft-single-M%d-v0'%i
    w_en = 'envs.grids.grid_environment:CraftRM10EnvM%d'%i
    register(
        id=w_id,
        entry_point=w_en,
        max_episode_steps=1000
    )

# ----------------------------------------- CAR2d

register(
    id='Car-2D-v0',
    entry_point='envs.car2d.car2d:MyVC_EnvRM1',
    max_episode_steps=1000
)


# ----------------------------------------- 9 ROOMS

register(
    id='Rooms9-M1-v0',
    entry_point='envs.rooms.rm_rooms:nine_rooms_half',
    max_episode_steps=1000
)

register(
    id='Rooms9-M2-v0',
    entry_point='envs.rooms.rm_rooms:nine_rooms_one',
    max_episode_steps=1000
)

# ----------------------------------------- 9 ROOMS Continuous Rewards

register(
    id='Rooms9C-M1-v0',
    entry_point='envs.rooms.rm_rooms:nine_rooms_half_continuous',
    max_episode_steps=1000
)


register(
    id='Rooms9C-M2-v0',
    entry_point='envs.rooms.rm_rooms:nine_rooms_one_continuous',
    max_episode_steps=1000
)


# ----------------------------------------- 16 ROOMS Few Doors

register(
    id='Rooms16-M1-v0',
    entry_point='envs.rooms.rm_rooms:sixteen_rooms_half',
    max_episode_steps=1000
)


register(
    id='Rooms16-M2-v0',
    entry_point='envs.rooms.rm_rooms:sixteen_rooms_one',
    max_episode_steps=1000
)

register(
    id='Rooms16-M3-v0',
    entry_point='envs.rooms.rm_rooms:sixteen_rooms_two',
    max_episode_steps=1000
)

# ----------------------------------------- 16 ROOMS Few Doors : Continuous

register(
    id='Rooms16C-M1-v0',
    entry_point='envs.rooms.rm_rooms:sixteen_rooms_half_continuous',
    max_episode_steps=1000
)


register(
    id='Rooms16C-M2-v0',
    entry_point='envs.rooms.rm_rooms:sixteen_rooms_one_continuous',
    max_episode_steps=1000
)

register(
    id='Rooms16C-M3-v0',
    entry_point='envs.rooms.rm_rooms:sixteen_rooms_two_continuous',
    max_episode_steps=1000
)


# ------------------------------------- Fetch

register(
    id = 'Fetch-M1-v0',
    entry_point = 'envs.mujoco_rm.fetch:fpp_goal',
    max_episode_steps = 1000
)

register(
    id = 'Fetch-M2-v0',
    entry_point = 'envs.mujoco_rm.fetch:fpp_fixed_goal',
    max_episode_steps = 1000
)
