import numpy as np
import pandas as pd


df = pd.DataFrame({'key':['a','b','c'] * 4, 'value':np.arange(12.)})
print(df)

g = df.groupby('key').value

print(g.mean())
print(g.transform(lambda x: x.mean()))
print(g.transform('mean'))
print(g.transform(lambda x: x.rank(ascending=False)))


def normalize(x):
    return ((x - x.mean()) / x.std())


print(g.transform(normalize))

N = 15

times = pd.date_range('2017-05-20 00:00', freq='1min', periods=N)

df = pd.DataFrame({'time':times, 'value':np.arange(N)})
print(df)

print(df.set_index('time').resample('5min').count())

df2 = pd.DataFrame({'time': times.repeat(3),'key': np.tile(['a', 'b', 'c'], N),
'value': np.arange(N * 3.)})
print(df2[0:7])


time_key = pd.TimeGrouper('5min')
resampled = (df2.set_index('time').groupby(['key', time_key]).sum())
print(resampled)
