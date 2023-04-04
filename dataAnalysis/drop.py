import pandas as pd
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)
meangrade = df['grade'].mean()

stdgrade = df['grade'].std()
toprange = meangrade + stdgrade * 1.96
botrange = meangrade - stdgrade * 1.96

copydf = df
copydf = copydf.drop(copydf[copydf['grade']>toprange].index)
copydf = copydf.drop(copydf[copydf['grade']
        < botrange].index)
print(copydf)