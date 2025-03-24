import gymnasium as gym
from PIL import Image
import datetime
import ale_py
import os 
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

if __name__ == '__main__':
    if not os.path.exists('envs_info/'):
        os.makedirs('envs_info')
    if not os.path.exists('envs_info/general'):
        os.makedirs('envs_info/general')
    if not os.path.exists('envs_info/phys2d'):
        os.makedirs('envs_info/phys2d')
    if not os.path.exists('envs_info/tabular'):
        os.makedirs('envs_info/tabular')
    if not os.path.exists('envs_info/ALE'):
        os.makedirs('envs_info/ALE')


    gym.register_envs(ale_py)
    current_gym_envs = gym.envs.registration.registry.keys()
    
    list_discrete_action_spaces_envs = []
    list_other_action_spaces = []
    list_discrete_obs_spaces_envs = []
    list_other_obs_spaces = []

    for env_name in current_gym_envs:
        if 'Joust' not in env_name and 'Warlords' not in env_name and 'MazeCraze' not in env_name and 'Combat' not in env_name and 'Reacher' not in env_name and 'Pusher' not in env_name and 'InvertedPendulum' not in env_name and 'InvertedDoublePendulum' not in env_name and 'Ant' not in env_name and 'HalfCheetah' not in env_name and 'Hopper' not in env_name and 'Walker2d' not in env_name and 'Swimmer' not in env_name and 'Humanoid' not in env_name and 'GymV21Environment' not in env_name and 'GymV26Environment' not in env_name:
            print(f"Environment Name: {env_name}")
            env = gym.make(env_name, render_mode='rgb_array')
            obs = env.reset()[0]
            datestr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            #print(datestr)
            img = Image.fromarray(env.render())

            if '/' not in env_name:
                env_name = f"general/{env_name}"
            img.save(f"envs_info/{env_name}_{datestr}.png")

            with open(f"envs_info/{env_name}_{datestr}.txt", 'w') as f:
                print(env_name, file=f)
                print("\nMetadata", file=f)
                print(env.metadata, file=f)
                print("\n\nAction Space", file=f)
                print(env.action_space, file=f)
                if isinstance(env.action_space, gym.spaces.Discrete):
                    list_discrete_action_spaces_envs.append((env_name, env.action_space))
                else:
                    list_other_action_spaces.append((env_name, env.action_space))
                print("\nObservation Space", file=f)
                print(env.observation_space, file=f)
                if isinstance(env.observation_space, gym.spaces.Discrete):
                    list_discrete_obs_spaces_envs.append((env_name,env.observation_space))
                else:
                    list_other_obs_spaces.append((env_name,env.observation_space))
                print("\nEnvironment Dictionary", file=f)
                print(env.__dict__, file=f)

                print("\n\nInitial Obervation", file=f)
                print(obs, file=f)
    print(f"-----------------------")
    print(f"Discrete Action Spaces Envs")
    for env_name in list_discrete_action_spaces_envs:
        print(env_name)
    print(f"-----------------------")
    print(f"Continuous Action Spaces Envs")
    for env_name in list_other_action_spaces:
        print(env_name)
    print(f"-----------------------")
    print(f"Discrete Observation Spaces Envs")
    for env_name in list_discrete_obs_spaces_envs:
        print(env_name)
    print(f"-----------------------")
    print(f"Continuous Action Spaces Envs")
    for env_name in list_other_action_spaces:
        print(env_name)
    print(f"-----------------------")