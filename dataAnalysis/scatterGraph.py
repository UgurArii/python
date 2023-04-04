import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.DataFrame({'Col':np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['Col'])