import pandas as pd
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)

df = df.sort_values(by='age', ascending=0)
print(df.head())