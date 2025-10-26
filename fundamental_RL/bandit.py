import numpy as np
import random
import matplotlib.pyplot as plt
k = 3
bandit = np.random.randint(low=1, high=100, size=k)
q = np.full(k,100).tolist()
a = 0.1
action_stat = []
q_his = []
epoch = []
def Action(values, eta):
    a = random.random()
    if(a<=eta): # exploratory move
        return random.randint(0, len(values)-1),1

    else:       # argmax 
        return values.index(max(values)),0
    
def evaluate(q,a,bandit,action):
    q[action] = q[action]+ a*(bandit[action]-q[action])    #action_value update
    return q
    
eta = 0.4

for i in range(500):
    choice,explore = Action(q,eta)
    q = evaluate(q,0.1,bandit,choice)
    q_his.append(q/bandit)
    epoch.append(i)
    action_stat.append(explore)

    print(f"For itiration {i+1} the updated values are {q}")

print(f"Final values are {q}, whereas bandit values are {bandit}")
plt.plot(epoch,q_his)
plt.scatter(epoch,action_stat,color='red')
plt.xlabel("EPOCH")
plt.ylabel("q/q*")
plt.title(f"learning over epoches eta= {eta}")
plt.show()

    
