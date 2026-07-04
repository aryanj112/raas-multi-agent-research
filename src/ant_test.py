import gymnasium as gym
from helper import save_video

# loads all the gymnasium stuff for the environment (still a bit confused on what all of this does and why we need to reset ask Kasra)
env = gym.make("Ant-v5")
obs, info = env.reset()

# we are not loading on mac since we might have issues with that so we will recreate a video
frames = []

for _ in range(300):
    # for the ant there are 8 simple actions that can be done and this will give us a vector of torques to each motor
    # random action which is why the ant flops (we get values from -1 to 1)
    action = env.action_space.sample()
    
    # ok so now we apply the action to it 
    # obs is the state we are in now that this action happened
    # reward is the value we get after that action based on the stuff embedded into the gym.make environment so that has all the info for the reward
    # terminated is if the thing fell into a position that is unrecoverable ahhhh
    # truncated is if we ran out of time steps (confused on this)
    obs, reward, terminated, truncated, info = env.step(action)

    frames.append(env.render())
    
    # good to just reset and stuff incase it fell over or stuff
    if terminated or truncated:
        obs, info = env.reset()

env.close()
save_video(frames, "random_ant.mp4", fps=30)
