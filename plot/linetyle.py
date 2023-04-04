# we import the Matplotlib library

import matplotlib as mlp
import matplotlib.pyplot as plt
"""
plt.plot([5,7,2,4])
plt.plot([5,7,2,4],[4,6,9,2], 'ro')
"""

x = [50,70,90,65]
y = [129, 192, 163, 172]
plt.plot(x, y, linewidth=4.0)

x1 = [50,70,90,65]
y1 = [129, 192, 163, 172]
plt.plot(x1, y1, linewidth = 4.0)

plt.plot(x1, y1, linewidth = 2.0, linestyle = '--')
plt.plot(x, y, linewidth = 1.0, ls = '-', marker = "o", markersize = 10)

plt.plot(x, y, linewidth = 1.0, ls = '-', marker = "o", markersize = 10, markerfacecolor = 'white')