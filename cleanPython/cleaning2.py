import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
index=['Ohio', 'Colorado', 'New York'],
columns=['one', 'two', 'three', 'four'])

transform = lambda x: x[:4].upper()
data.index.map(transform)

data.index = data.index.map(transform)
print(data)
print(data.rename(index=str.title, columns=str.upper))

print(data.rename(index={'OHIO':'INDIANA'}, columns={'three':'peekaboo'}))
data.rename(index={'OHIO':'INDIANA'}, inplace=True)
print(data)

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32,67]
bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages, bins)
print(cats)
print(cats.codes)
print(cats.categories)
print(pd.value_counts(cats))
print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels=group_names))

data1 = np.random.randn(1000)
cats1 = pd.qcut(data1,4)
print(cats1)
print(pd.value_counts(cats))

data2 = pd.DataFrame(np.random.randn(1000, 4))
print(data2.describe)
col = data2[2]
print(col[np.abs(col)>3])
print(data2[(np.abs(data2)>3).any(1)])
print(np.sign(data2).head())