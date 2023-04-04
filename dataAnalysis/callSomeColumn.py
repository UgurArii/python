import pandas as pd
import numpy as np
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)
print(df.head())
df2 = df[['fname','age','grade']]
df2['fullname'] = df['fname'] + " " + df['lname']
print(df2.head())
print(df2['fullname'])

