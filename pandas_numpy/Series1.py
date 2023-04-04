import numpy as np
import pandas as pd

Series1 = pd.Series(np.random.randn(4), index=['a','b','c','d'])
print(Series1)
print(Series1.index)

print("\n CREATE SERIES FROM SCALAR VALUE")
Sc1 = pd.Series(8., index=['a','b','c','d'])
print(Sc1)

dict1 = {'one' : pd.Series([1., 2., 3.],
index=['a', 'b', 'c']),
'two' : pd.Series([1., 2., 3., 4.],
index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(dict1)
print(df)

print(pd.DataFrame(dict1, index=['d','b','a']))
print(pd.DataFrame(dict1, index=['d', 'b', 'a'], columns=['two','three', 'one']))


data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
data[:] = [(1,2.,'Hello'),(2,3.,'World')]
print(pd.DataFrame(data))

print(pd.DataFrame(data, index=['First','Second']))
print(pd.DataFrame(data, columns=['C','A','B']))

