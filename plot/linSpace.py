from numpy import *
import math
import matplotlib.pyplot as plt

t = linspace(0, 2*math.pi, 400)
a = sin(t)
b = cos(t)
c = a + b 

plt.plot(t, a, 'r')
plt.plot(t, b, 'b')
plt.plot(t, c, 'g')
plt.show()
