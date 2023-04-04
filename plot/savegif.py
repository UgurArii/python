import matplotlib.pyplot as plt
import numpy as np

x, y = [1600, 1700, 1800, 1900, 2000], [0.2,0.5,1.1,2.2,7.7]
plt.plot(x,y, "bo-")
plt.title("World Population OVer Time")
plt.xlabel("Year")
plt.ylabel("Population(billions")
plt.savefig("population.jpg")