import matplotlib.pyplot as plt
import numpy as np

florida =[np.random.normal(loc=60, scale=15) for x in range(1000)]
california = [np.random.normal(loc=35, scale=5) for x in range(1000)]

plt.hist(florida, bins=45, color="r", alpha=0.4)
plt.show()
# chart 2
plt.hist(california, bins=45, color="b", alpha=0.4)
plt.show()

# chart 3
plt.hist(florida, bins=45, color="r", alpha=0.7) 

plt.hist(california, bins=45, color="b", alpha=0.7)
plt.show()