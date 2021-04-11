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
    id='Rooms9-v0',
    entry_point='envs.rooms.rm_rooms:nine_rooms',
    max_episode_steps=1000
)

# ----------------------------------------- 16 ROOMS Few Doors

register(
    id='Rooms16-v0',
    entry_point='envs.rooms.rm_rooms:sixteen_rooms_fewdoors1',
    max_episode_steps=1000
)

# ----------------------------------------- 16 ROOMS More Doors

register(
    id='Rooms16-v1',
    entry_point='envs.rooms.rm_rooms:sixteen_rooms_moredoors1',
    max_episode_steps=1000
)

