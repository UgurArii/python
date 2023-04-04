import pandas as pd
import numpy as np

df4 = pd.DataFrame({'Date': ['2017-01-01', '2017-01-01','2017-01-02', '2017-01-01', '2017-01-02', '2017-01-02', '2017-­01-­03', '2017-01-02', '2017-01-03', '2017-01-03'],
'Type':['x', 'x', 'y', 'x', 'y', 'x', 'z',
'y', 'z', 'y'],
'Value':[185, 265, 168, 245, 143, 172, 346,
285, 145, 128],
                   })

print(df4)

print(pd.pivot_table(df4, index="Date", values="Value", columns="Type"))
df5 = pd.pivot_table(df4, index="Date", values="Value", columns="Type")
print(df5.dropna().shape)

print(pd.notnull(df5))

print(df5.isnull().sum())

print(df5.dropna())
print(df5.dropna(axis=1, how='any'))
print(df5.fillna(0))
print(df5.fillna('Invalid'))
print(df5.fillna(df5.mean()))