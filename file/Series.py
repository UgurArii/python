import pandas as pd
import numpy as np

data = np.array(['O','S','S','A'])
S1 = pd.Series(data)
S2 = pd.Series(data, index=[100,101,102,103])
print(S1)
print()
print(S2)

data1 = {'X': 0., 'Y':1., 'Z':2.}
SERIES1 = pd.Series(data)
print(SERIES1)
Series1 = pd.Series([1,2,3,4,5],index =
                             ['a','b','c','d','e'])
print ("Example 1:Retrieve the first element")
print (Series1[0] )
print ("\nExample 2:Retrieve the first three element")
print (Series1[:3])
print ("\nExample 3:Retrieve the last three element")
print(Series1[-3:])
print ("\nExample 4:Retrieve a single element")
print (Series1['a'])
print ("\nExample 5:Retrieve multiple elements")
print (Series1[['a','c','d']])

my_series1 = pd.Series([5,6,7,8,9,10])
print("my_series1\n", my_series1)
print("\n Series Analysis\n")
print("Series mean value: ", my_series1.mean())
print("Series max value: ", my_series1.max())
print('Series min value:', my_series1.min())
print('Series standar deviation value: ',my_series1.std())
my_series1 = pd.Series([5, 6, 7, 8, 9, 10])
my_series_11 = my_series1.copy()
def AddSeries(x,y):
    for i in range(len(x)):
        print(x[i] + y[i])
print("Add two series\n")
AddSeries(my_series1,my_series1)

import matplotlib.pyplot as plt
plt.plot(my_series2)
plt.ylabel('index')
plt.show()