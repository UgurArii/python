import matplotlib.pyplot as plt
import numpy as np
from random import randint
import random
random.seed(2)
height = [randint(58, 78) for x in range(20)]
weight = [randint(90, 250) for x in range(20)]
age = [randint(18,65) for x in range(20)]
plt.scatter(weight, height, c=age)

plt.title("Height-WEight Distribution")
plt.xlabel("Weight(lbs")
plt.ylabel("Height(inches)")
plt.colorbar(label="Age")
plt.show()




