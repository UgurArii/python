import pandas as pd
import numpy as np

df = pd.DataFrame({'key':['b','b','a','c','a','b'],
                   'data':range(6)})

print(pd.get_dummies(df['key']))
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data']].join(dummies)

print(df_with_dummy)
