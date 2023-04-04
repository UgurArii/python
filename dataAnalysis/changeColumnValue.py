import pandas as pd
import numpy as np
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)
df.columns = ['FirstName', 'LastName', 'Gender',
        'Age', 'HoursExercisePerWeek',
        'HoursStudyPerWeek', 'LetterGrade',
        'StreetAddress']
print(df.head())
headers = list(df.columns.values)

headers[0] = 'FName'
headers[1] = 'LName'
df.columns = headers
print(df.head())




