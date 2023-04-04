import pandas as pd
import numpy as np
from numpy import nan as NA
df = pd.DataFrame(np.random.rand(7,3))
df.iloc[:4,1] = NA
df.iloc[:2,2] = NA
print(df)
print(df.dropna())
print(df.dropna(thresh=2))
print(df.fillna(0))
print(df.fillna({1:0.5, 2:0}))
print(df.fillna(0, inplace=True))

df1 = pd.DataFrame(np.random.randn(6, 3))

df1.iloc[2:,1] = NA
df1.iloc[4:,2] = NA
print(df1)
print(df1.fillna(method='ffill'))
print(df1.fillna(method='ffill', limit=2))
data = pd.Series([1., NA, 3.5, NA, 7])
print(data.fillna(data.mean()))
data1 = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data1.duplicated())
data2 = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
'Pastrami', 'corned beef', 'Bacon','pastrami', 'honey ham', 'nova lox'],'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data2)
meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}

lowercased = data2['food'].str.lower()
print(lowercased)
data2['animal'] = lowercased.map(meat_to_animal)
print(data2)
#print(data['food'].map(lambda x: meat_to_animal[x.lower()]))

data3 = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data3)
print(data3.replace([-999,-1000], [np.nan, 0]))




























