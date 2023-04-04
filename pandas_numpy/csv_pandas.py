import pandas as pd

df2 = pd.read_csv("/root/Desktop/pythonTest/addresses.csv")
print(df2)

df2 = pd.read_csv("/root/Desktop/pythonTest/addresses.csv", header=None)
print(df2)
"""
df2 = pd.read_csv("/root/Desktop/pythonTest/addresses.csv", header=1)
print(df2)"""

df2 = pd.read_csv("/root/Desktop/pythonTest/addresses.csv", names = ['var1','var2' 'var3', 'var4'])
print(df2)