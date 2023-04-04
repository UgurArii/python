import pandas  as pd
import numpy as np

print(pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
            ('a', 'a'): {('A', 'C'): 3, ('A','B'): 4},
            ('a', 'c'): {('A', 'B'): 5, ('A','C'): 6},
            ('b', 'a'): {('A', 'C'): 7, ('A','B'): 8},
            ('b', 'b'): {('A', 'D'): 9, ('A','B'): 10}}))

ndarrdict = {'one':[1.,2.,3.,4.],'two':[4.,3.,2.,1.]}
df = pd.DataFrame(ndarrdict, index=['a','b','c','d'])
print(df)
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
print(df)
df['Filler'] = 'HCT'
df['Slic'] = df['one'][:2]
print(df)
del df['two']
Three = df.pop('three')
print(df)
df.insert(1, 'bar',df['one'])
print(df)
