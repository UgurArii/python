import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df2 = np.random.randn(100)
df3 = np.random.randn(100)

plt.hist(df2, color="red", alpha = 0.3, bins=15)
plt.hist(df3, alpha=0.6, bins=15)