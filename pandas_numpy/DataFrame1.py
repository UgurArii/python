import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np

obj = pd.Series([4, 7, -5, -3],index=['d', 'b', 'a', 'c'])

print(obj)
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002, 2003],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data)
print(frame)
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
index=['one', 'two', 'three', 'four','five', 'six'])

print(frame2)
print(frame2.loc['three'])

frame2['debt'] = 16.5
print(frame2)

frame2['debt'] = np.arange(6.)
print(frame2)
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)