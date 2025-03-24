import gymnasium as gym
from PIL import Image
import datetime
import ale_py
import os 

if __name__ == '__main__':
    if not os.path.exists('envs_info'):
        os.makedirs('envs_info')
    if not os.path.exists('envs_info/phys2d'):
        os.makedirs('envs_info/phys2d')
    if not os.path.exists('envs_info/tabular'):
        os.makedirs('envs_info/tabular')
    if not os.path.exists('envs_info/ALE'):
        os.makedirs('envs_info/ALE')
    #env_name = "CartPole-v1"
    gym.register_envs(ale_py)
    current_gym_envs = gym.envs.registration.registry.keys()
    
    for envname in current_gym_envs:
        print(envname)
    print(f"-----------------------")
    for env_name in current_gym_envs:
        if 'Joust' not in env_name and 'Warlords' not in env_name and 'MazeCraze' not in env_name and 'Combat' not in env_name and 'Reacher' not in env_name and 'Pusher' not in env_name and 'InvertedPendulum' not in env_name and 'InvertedDoublePendulum' not in env_name and 'Ant' not in env_name and 'HalfCheetah' not in env_name and 'Hopper' not in env_name and 'Walker2d' not in env_name and 'Swimmer' not in env_name and 'Humanoid' not in env_name and 'GymV21Environment' not in env_name and 'GymV26Environment' not in env_name:
            print(f"Environment Name: {env_name}")
            env = gym.make(env_name, render_mode='rgb_array')
            obs = env.reset()[0]
            datestr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            #print(datestr)
            img = Image.fromarray(env.render())
            img.save(f"envs_info/{env_name}_{datestr}.png")

            with open(f"envs_info/{env_name}_{datestr}.txt", 'w') as f:
                print(env_name, file=f)
                print("env.reset() Obervation")
                print(obs, file=f)
                print(env.__dict__, file=f)