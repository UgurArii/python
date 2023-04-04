import pandas as pd
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)

df['graderanked'] = df['grade'].rank(ascending=1)
print(df.tail)

print(df[df['graderanked']<21])

print(df[df['graderanked'] < 6].sort_values('graderanked'))