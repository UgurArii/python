import pandas as pd
import numpy as np
import re

data = pd.Series(np.random.randn(9),
index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
[1, 2, 3, 1, 3, 1, 2, 2, 3]])

print(data.index)
print(data.loc['b':'c'])
print(data.loc[:,2])
print(data.unstack().stack())



