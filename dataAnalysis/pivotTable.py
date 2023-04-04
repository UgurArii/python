import pandas as pd
import statsmodels.formula.api as sm
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)

print(pd.pivot_table(df, index=['gender']))
print(pd.pivot_table(df, values=['grade'], index=['gender']))
print(pd.pivot_table(df, values=['grade'], index=['gender'], aggfunc='min'))
print(pd.pivot_table(df, index=['gender','age'], aggfunc='max', values=['hours']))

print(pd.pivot_table(df,
        index=['gender'],
        aggfunc='mean',
        values=['grade','hours']))

df2 = df.loc[df['age'] == 17]
print(pd.pivot_table(df2, index=['gender'],
                     aggfunc='mean', values=['grade', 'hours']))

print(pd.pivot_table(df2,
        index=['gender'],
        aggfunc='mean',
        values=['grade','hours'],
        margins='True'))