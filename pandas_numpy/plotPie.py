import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

col1 = ["yellow","red","purple","orange"]
x = [10,50,78,50]
lab1 = ['A','B','C','D']
ex1 = [0.5,0,0,1]
plt.pie(x, colors = col1, labels= lab1, explode=ex1)

df1 = pd.DataFrame(np.random.rand(10, 4), columns =
['var1', 'var2', 'var3', 'var4'])

df1.plot(kind="bar")
df1.plot(kind="bar", stacked=True)
df1.hist()

df1['var1'].hist()


df1.loc[1].hist()
df1.boxplot(return_type="axes")

df1.plot(kind="area",color=col1)
df1.plot(kind="scatter",x="var3", y="var4")
plt.savefig('graph.png', dpi=600)

print(plt.style.available)

plt.style.use('dark_background')
df1.plot(kind="area")

plt.style.use("seaborn-darkgrid")
df1.plot(kind="area")


