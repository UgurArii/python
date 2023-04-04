import pandas as pd
import numpy as np
iris = pd.read_csv("/root/Desktop/pythonTest/iris.data")

print(iris.head(3))
jf = pd.DataFrame(np.arange(16).reshape(4,4), index=['A','B','C','D'], columns = ['var1','var2','var3','var4'])

print(jf)