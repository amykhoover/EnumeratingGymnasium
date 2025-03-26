import gymnasium as gym
from PIL import Image
import datetime
import ale_py
import os 
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
#gym.register_envs(ale_py)
#current_gym_envs = gym.envs.registration.registry.keys()
#     if 'Joust' not in env_name and 'Warlords' not in env_name and 'MazeCraze' not in env_name and 'Combat' not in env_name and 'Reacher' not in env_name and 'Pusher' not in env_name and 'InvertedPendulum' not in env_name and 'InvertedDoublePendulum' not in env_name and 'Ant' not in env_name and 'HalfCheetah' not in env_name and 'Hopper' not in env_name and 'Walker2d' not in env_name and 'Swimmer' not in env_name and 'Humanoid' not in env_name and 'GymV21Environment' not in env_name and 'GymV26Environment' not in env_name:



def run_environment(env_id, num_episodes=1, max_steps=500, render_mode="human"):
    print(f"\nRunning environment: {env_id}")
    env = gym.make(env_id, render_mode=render_mode)
    
    for episode in range(num_episodes):
        obs, info = env.reset()
        for step in range(max_steps):
            env.render()
            action = env.action_space.sample()
            obs, reward, terminated, truncated, info = env.step(action)
            if terminated or truncated:
                print(f"Episode ended after {step+1} steps.")
                break
            time.sleep(0.02)  
    env.close()


def print_env_info(env_id, path):
    print(f"\nRunning environment: {env_id}")
    datestr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    env = gym.make(env_id, render_mode="rgb_array")
    obs, info = env.reset()

    img = Image.fromarray(env.render())
    img.save(f"{path}/{env_id}_{datestr}.png")

    with open(f"{path}/{env_id}_{datestr}.txt", 'w') as f:
        print(env_id, file=f)
        print("Initial Obervation", file=f)
        print(obs, file=f)
        print("Action Space", file=f)
        print(env.action_space, file=f)
        print("Observation Space", file=f)
        print(env.observation_space, file=f)
        print("\nMetadata", file=f)
        print(env.metadata, file=f)
        print("\nEnvironment Dictionary", file=f)
        print(env.__dict__, file=f)
    env.close()


env_dict = {
    "classic_control": ['CartPole-v1', 'MountainCar-v0', 'Acrobot-v1', 'MountainCarContinuous-v0','Pendulum-v1'],
    "phys2d": ['phys2d/CartPole-v0', 'phys2d/CartPole-v1', 'phys2d/Pendulum-v' ],
    #"mujoco": ['Ant', 'HalfCheetah', 'Hopper', 'Humanoid', 'InvertedDoublePendulum', 'InvertedPendulum','Pusher','Reacher','Swimmer' , 'Walker2d'],
    "mujoco/manipulation":["Reacher-v2","Reacher-v4","Reacher-v5", "Pusher-v2","Pusher-v4","Pusher-v5"],
    "mujoco/balance": ["InvertedPendulum-v2","InvertedPendulum-v4","InvertedPendulum-v5","InvertedDoublePendulum-v2","InvertedDoublePendulum-v4","InvertedDoublePendulum-v5"],
    "mujoco/runners": ["HalfCheetah-v2","HalfCheetah-v3","HalfCheetah-v4", "HalfCheetah-v5","Hopper-v2","Hopper-v3","Hopper-v4","Hopper-v5","Swimmer-v2","Swimmer-v3","Swimmer-v4","Swimmer-v5","Walker2d-v2","Walker2d-v3","Walker2d-v4","Walker2d-v5","Ant-v2","Ant-v3","Ant-v4","Ant-v5","Humanoid-v2","Humanoid-v3","Humanoid-v4","Humanoid-v5","HumanoidStandup-v2","HumanoidStandup-v3","HumanoidStandup-v4","HumanoidStandup-v5"],
    "tabular": ["CliffWalking-v0"],
    "toy_text": ["Blackjack-v1","FrozenLake-v1","FrozenLake8x8-v1","CliffWalking-v0","Taxi-v3"]
}

output_dir_root = "envs_info_test"

if __name__ == '__main__':

    for key in env_dict.keys():
        print(f"{key}")
        if 'phys2d' not in key  and "mujoco" not in key:
            folder_name = f"{output_dir_root}/{key}"
            if not os.path.exists(f"{output_dir_root}/{key}"):
                os.makedirs(folder_name) #like the -p option in mkdir
    
    for key in env_dict.keys():
        print(f"{key}")
        folder_name = f"{output_dir_root}/{key}"
        if 'phys2d' not in key  and "mujoco" not in key:
            for game in env_dict[key]:
                print(f"{game}, {folder_name }")
                print_env_info(game,folder_name)

