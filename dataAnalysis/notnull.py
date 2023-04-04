import pandas as pd
import numpy as np
Location = "/root/Desktop/pythonTest/gradedata.csv"

df = pd.read_csv(Location)

print(df['grade'].head())
print(df[['age','grade']].head())
print(df[:2])
print(df[df['grade']>80])

female = df['gender'] == "female"
a_student = df['grade'] >= 90
print(df[female & a_student].head())
print(df[df['fname'].notnull() & (df['gender'] == "male")].head())