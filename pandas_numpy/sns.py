import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use('classic')
plt.style.use('seaborn-whitegrid')

#create some data
data = np.random.multivariate_normal([0,0], [[5,2],[2,2]], size=2000)
data = pd.DataFrame(data, columns=['x','y'])

#plot the data with seaborn
sns.distplot(data['x'])
sns.distplot(data['y'])

for col in 'xy':
    sns.kdeplot(data[col], shade=True)

with sns.axes_style('white'):
    sns.jointplot("x","y", data, kind='kde')
    
with sns.axes_style('white'):
    sns.jointplot("x","y",data, kind='hex')
    
sns.pairplot(data)