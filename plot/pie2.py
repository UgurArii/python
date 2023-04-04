import matplotlib.pyplot as plt


days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]
slices = [39,14,26,41]
activities = ['sleeping', 'eating', 'working','playing']
cols = ['c','m','r','b','g']
plt.pie(slices, labels = activities, colors=cols,startangle=100, shadow=True,
        explode = (0.0,0.0,0.09,0),
        autopct = '%1.1f%%')
plt.title('Persons Weekly Spent Time per activities\nSpring 2018')
plt.legend()
plt.show()





