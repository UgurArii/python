import numpy as np
import pandas as pd
import patsy

data = pd.DataFrame({'x0':[1,2,3,4,5],
                     'x1':[0.1, -0.01, 0.25, -4.1, 0.],
                     'y': [-1.5, 0., 3.6, 1.3, -2.]})

print(data)
print(data.columns)
print(data.values)
df2 = pd.DataFrame(data.values, columns=['one', 'two', 'three'])
print(df2)

df3 = df2.copy()
df3['strings'] = ['a', 'b', 'c', 'd', 'e']

print(df3.values)

data['category'] = pd.Categorical(['a','b','a','a','b'], categories=['a','b'])
print(data)

dummies = pd.get_dummies(data.category, prefix='category')
data_with_dummies = data.drop('category', axis=1).join(dummies)

print(data_with_dummies)

data1 = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a', 'b', 'a', 'b'],'key2': [0, 1, 0, 1, 0, 1, 0, 0],
'v1': [1, 2, 3, 4, 5, 6, 7, 8],'v2': [-1, 0, 2.5, -0.5, 4.0, -1.2, 0.2, -1.7]})

y, X = patsy.dmatrices('v2 ~ key1', data1)

print(X)

y, X = patsy.dmatrices('v2 ~ key1 + 0', data1)
print(X)

y, X = patsy.dmatrices('v2 ~ C(key2)', data1)
print(X)

data1['key2'] = data1['key2'].map({0:'zero', 1:'one'})
print(data1)
y, X = patsy.dmatrices('v2 ~ key1 + key2', data1)
print(X)
y, X = patsy.dmatrices('v2 ~ key1 + key2 + key1:key2', data1)
print(X)

