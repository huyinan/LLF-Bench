import gymnasium as gym
import llfbench

# env = gym.make('llf-PickBestSummary-v0')

loss_env = gym.make('llf-Booth-v0', feedback=1)

action = """
x = [-4.0, 5.0]
"""

assignment = loss_env.reset()
observation, reward, done, truncated, info = loss_env.step(action)

print('Assignment: ', assignment, '\n', \
      'Observation: ', observation, '\n', \
      'Reward: ', reward, '\n', \
      'Done: ', done, '\n', \
      'Info: ', info)

loss_env = gym.make('llf-Booth-b-hp-v0')

action = """
x = [-4.0, 5.0]
"""

assignment = loss_env.reset()
observation, reward, done, truncated, info = loss_env.step(action)

print('Assignment: ', assignment, '\n', \
      'Observation: ', observation, '\n', \
      'Reward: ', reward, '\n', \
      'Done: ', done, '\n', \
      'Info: ', info)
