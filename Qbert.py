#!usr/bin/env python
import gym
env = gym.make('Qbert-v0')
MAX_NUM_EPISODES = 10
MAX_STEPS_PER_EPISODES = 500
for episodes in range(MAX_NUM_EPISODES):
    obs = env.reset()
    for step in range(MAX_STEPS_PER_EPISODES):
        env.render()
        action = env.action_space.sample()
        next_state,reward,done,info = env.step(action)
        obs = next_state

        if done is True:
            print("<nEpisode #{} ended in {} steps." 
            . format(episodes,step+1))
            break