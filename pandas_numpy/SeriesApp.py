import numpy as np
import pandas as pd

series1 = pd.Series(np.random.randn(7))
series1.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(series1)

series5 = pd.Series(np.random.randn(7))

s15 = pd.concat([series1,series5])
print(s15)
