import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[], color='m', label='Sleeping')
plt.plot([],[], color='c', label='Eating')
plt.plot([],[], color='r', label='Working')
plt.plot([],[], color='k', label='Playing')

plt.stackplot(days, sleeping, eating, working ,
playing, colors=['m','c', 'r', 'k'])
plt.xlabel('days')
plt.ylabel('Activities')
plt.title('Persons Weekly Spent Time per activities\nSpring 2018')
plt.legend()
plt.show()
