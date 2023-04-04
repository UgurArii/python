import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5)
ages=[np.random.normal(loc=40, scale=10) for x in range(1000)]
plt.hist(ages, bins=45)
plt.title("Ages per Population")
plt.xlabel("Age")
plt.ylabel("# of People")
plt.show()





