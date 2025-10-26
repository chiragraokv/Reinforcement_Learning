import numpy as np
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

class Bandit:
    def __init__(self,arms,eta):
        self.k = arms
        self.q = np.zeros(arms).tolist()
        self.std_div = 1
        self.eta = eta
        self.action_count = np.zeros(self.k).tolist()

    def Action(self):
        a = random.random()
        if(a<=self.eta): # exploratory move
            return random.randint(0, len(self.q)-1)

        else:       # argmax 
            ties = []
            top_value = float("-inf")
            for i in range(len(self.q)):
                if(self.q[i]>top_value):
                    top_value = self.q[i]
                    ties = [i]
                elif(self.q[i] == top_value):
                    ties.append(i)

            return random.choice(ties)
    
    def evaluate(self,action):
        reward = np.random.normal(loc=self.means[action], scale=self.std_div)
        self.action_count[action] += 1
        self.q[action] = self.q[action]+ (1/self.action_count[action])*(reward-self.q[action])    #action_value update
        return reward
    def Run(self,itr):
        self.means = np.random.normal(0,1,size=self.k)
        self.q = np.zeros(self.k).tolist()
        self.action_count = np.zeros(self.k).tolist()

        reward = []
        for i in range(itr):
            act = self.Action()
            r = self.evaluate(act)
            reward.append(r)
        return np.array(reward)
    
    






