import numpy as np
import pandas as pd
import matplotlib as mpl


data = { 'Animal': ['cat', 'cat', 'snake', 'dog', 'dog',
                 'cat', 'snake', 'cat', 'dog', 'dog'],
'Age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
'Visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'Priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no',
'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels, columns=['Animal','Age','Priority','Visits'])
print(df)
print(df.info(), "\n", df.describe())
print(df.iloc[:3])
print(df[['Animal','Age']])
print(df.groupby('Priority')['Animal'].count())
print(df.groupby('Animal')['Age'].mean())
print(df.groupby('Animal')['Age'].describe())



