import pandas as pd
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)
q1 = df['grade'].quantile(.25)
q3 = df['grade'].quantile(.75)
iqr = q3 - q1
toprange = q3 + iqr * 1.5
botrange = q1 - iqr * 1.5
copydf = df
copydf = copydf.drop(copydf[copydf['grade']
        > toprange].index)
copydf = copydf.drop(copydf[copydf['grade']
        < botrange].index)
print(copydf)