import pandas as pd

df1 = pd.DataFrame({'Names': ['Simon', 'Kate', 'Francis',
'Laura', 'Mary', 'Julian', 'Rosie'],
        'Height':[180, 165, 170, 164, 163, 175, 166],
        'Weight':[85, 65, 68, 45, 43, 72, 46],
         'Pref_food':['steak', 'pizza', 'pasta', 'pizza', 'vegetables','steak','seafood'],
        'Sex':['m', 'f','m','f', 'f', 'm', 'f']})
print(df1)
print(df1.describe())
print(df1.columns)
"""
print(df1.set_index('Names'))
print(df1.set_index('Names', inplace = True))"""
print(df1.shape)
print(df1.dtypes)
print(df1.head())
print(df1.tail(3))
print(df1.info())
print(df1.sort_values(by='Weight', ascending=False))
print(df1.sort_values(by='Weight', na_position="last"))
print(df1.sort_values(by='Weight', na_position="first"))

print(df1[::2])
print(df1[df1.Height > 170])
print(df1.query("Sex != 'f'"))
df1 = df1.rename(columns = {'Pref_food': 'Food'})
print(df1)
df2 = df1.copy()
df2['new_col'] = df2.Height/100
print(df2)
print(df1.groupby('Sex'))

grouped1 = df1.groupby('Sex')
print(grouped1.groups)

for names, groups in grouped1:
    print(names)
    print(groups)
grouped2 = df1.groupby(['Sex', 'Food'])
print(grouped2.groups)
print(grouped2.size())
print(grouped2.describe())
print(df1['Sex'].value_counts())
print(pd.crosstab(df1.Sex, df1.Food, margins=True))
