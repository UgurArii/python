import pandas as pd
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)
print(df.head())
# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]
# Create names for the four groups
group_names = ['F', 'D', 'C', 'B', 'A']

df['letterGrades'] = pd.cut(df['grade'],
        bins, labels=group_names)
print(df)