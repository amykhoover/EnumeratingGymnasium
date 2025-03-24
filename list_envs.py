import gymnasium as gym
from PIL import Image
import datetime
import ale_py
import os 

if __name__ == '__main__':    
    
    gym.register_envs(ale_py)
    current_gym_envs = gym.envs.registration.registry.keys()

    for envname in current_gym_envs:
        #print(envname)
        if '/' not in envname:
            print(envname)
    print(f"-----------------------")


    # for env_name in current_gym_envs:
    #     if 'Joust' not in env_name and 'Warlords' not in env_name and 'MazeCraze' not in env_name and 'Combat' not in env_name and 'Reacher' not in env_name and 'Pusher' not in env_name and 'InvertedPendulum' not in env_name and 'InvertedDoublePendulum' not in env_name and 'Ant' not in env_name and 'HalfCheetah' not in env_name and 'Hopper' not in env_name and 'Walker2d' not in env_name and 'Swimmer' not in env_name and 'Humanoid' not in env_name and 'GymV21Environment' not in env_name and 'GymV26Environment' not in env_name:
