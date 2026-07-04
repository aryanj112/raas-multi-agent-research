import gymnasium as gym
from stable_baselines3 import PPO

from helper import save_video

# env = gym.make("Ant-v5")


# model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="../logs/ant_tensorboard")
# model.learn(total_timesteps=200_000)
# model.save("ppo_ant")




model = PPO.load("ppo_ant")
env = gym.make("Ant-v5", render_mode="rgb_array")

obs, info = env.reset()
frames = []
for _ in range(500):
    action, _ = model.predict(obs)
    obs, reward, terminated, truncated, info = env.step(action)
    frames.append(env.render())
    if terminated or truncated:
        obs, info = env.reset()

save_video("trained_ant.mp4", frames, fps=30)