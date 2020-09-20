#!usr/bin/env python
import gym
env = gym.make('MountainCar-v0')
MAX_NUM_EPISODES = 20
#MAX_STEPS_PER_EPISODES = 500
for episodes in range(MAX_NUM_EPISODES):
    done = False
    obs = env.reset()
    total_reward = 0.0
    step = 0
    while not done:
        env.render()
        action = env.action_space.sample()
        next_state,reward,done,info = env.step(action)
        total_reward +=reward
        #print(total_reward)
        step +=1
        obs = next_state

        if done is True:
            print("<nEpisode #{} ended in {} steps {} rewards." 
            . format(episodes,step+1,total_reward))
            break
env.close()