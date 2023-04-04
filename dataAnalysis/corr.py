import pandas as pd
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)
print(df.head())
print(df.corr())