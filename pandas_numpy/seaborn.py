import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

#Create empty figure
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)

ax.plot(x, np.sin(x))
plt.plot(x, np.sin(x))
plt.plot(x, np.cos())

#set the x and y axis range
plt.xlim(0,11)
plt.ylim(-2,2)
plt.axis('tight')

#add title
plt.title('Plotting data using sin and cos')


