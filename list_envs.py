import gymnasium as gym
from PIL import Image
import datetime
import ale_py
import os 

if __name__ == '__main__':    
    
    gym.register_envs(ale_py)
    current_gym_envs = gym.envs.registration.registry.keys()
    for envname in current_gym_envs:
        print(envname)
    print(f"-----------------------")