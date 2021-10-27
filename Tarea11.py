import random
import seaborn as sns
import matplotlib.pyplot as plt


interations = 10000
variables = ['salary', 'conditions', 'location', 'job_security']

def Monte_Carlo(grade):
    final_results = []
    weight = [0.25, 0.25, 0.25, 0.25]
    for n in range(interations):
        results = []
        for i in range(len(variables)):
            value = weight[i] * (random.uniform(grade[i][0], grade [i][1]))
            results.append(value)
        final_results.append(sum(results))
    return final_results

a = Monte_Carlo([[7, 9], [2, 6], [8, 9.5], [5, 9]])
b = Monte_Carlo([[5, 7], [4, 6], [6, 9], [7, 8]])
c = Monte_Carlo([[6, 8], [3, 5], [8, 10], [6, 7]])

fig=plt.figure(figsize=(10,6))

sns.displot(a)
sns.displot(b)
sns.displot(c)
fig.legend(labels=['Job A', 'Job B', 'Job C'])
plt.title('Monte-Carlo Distributions')
plt.show()