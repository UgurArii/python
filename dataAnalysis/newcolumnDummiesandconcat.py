import pandas as pd
import numpy as np
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)

print(df.head())

def score_to_numeric(x):
    if x=='female':
        return 1
    if x=='male':
        return 0
df['gender_val'] = df['gender'].apply(score_to_numeric)
print(df.tail)

df_gender = pd.get_dummies(df['gender'])
print(df_gender.tail())

# Join the dummy variables to the main dataframe
df_new = pd.concat([df, df_gender], axis=1)
print(df_new.tail())

# Alterative for joining the new columns
df_new = df.join(df_gender)
print(df_new.tail())