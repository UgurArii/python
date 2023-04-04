import matplotlib.pyplot as plt
from random import randint
import random
random.seed(2)
height = [randint(58, 78) for x in range(20)]

weight = [randint(90,250) for x in range(20)]

plt.scatter(weight, height)
plt.title("Height-Weight Distribution")
plt.xlabel("Weight(lbs)")
plt.ylabel("Height(inches)")
plt.show()
