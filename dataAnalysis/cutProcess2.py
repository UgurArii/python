import pandas as pd
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)

# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]
# Create names for the four groups
group_names = ['F', 'D', 'C', 'B', 'A']
df['letterGrades'] = pd.cut(df['grade'],
        bins, labels=group_names)
print(df.groupby('letterGrades')['hours'].mean())
df['grade'] = df['grade'] = df['grade'].apply(lambda x: int(x))

print(df.head)

gender_preScore = df['grade'].groupby(df['gender'])
print(gender_preScore.mean())