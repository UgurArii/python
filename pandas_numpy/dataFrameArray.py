import numpy as np
import pandas as pd
from numpy import *
import matplotlib.pyplot as plt

arr1 = np.array([0,1,2,3,4])
print(arr1)

arr3 = np.arange(100)
print(arr3)
x = np.random.rand(1000)
plt.hist(x, bins=100)
plt.show()

rdf = pd.DataFrame(np.random.randn(10,5))
print(rdf)

var_names = ['var1','var2','var3','var4','var5']

rdf.columns = var_names

print(rdf.head())
rdf_bin = pd.DataFrame(np.random.binomial(100, 0.5,(10,5)))

print(rdf_bin)

# Poisson distribution

rdf_poi = pd.DataFrame(np.random.poisson(100,(10,5)))
print(rdf_poi)

# uniform distribution
rdf_un = pd.DataFrame(np.random.uniform(1,100,(10,5)))
print(rdf_un)

tos = pd.DataFrame(np.random.randn(10,5))

np.save('tos_saved', tos)

load1 = np.load('tos_saved.py')


























