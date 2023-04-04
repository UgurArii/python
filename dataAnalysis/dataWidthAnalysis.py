import pandas as pd
import statsmodels.formula.api as sm
Location = "/root/Desktop/pythonTest/gradedata.csv/"
df = pd.read_csv(Location)

print(df.mode().transpose())

data_types = pd.DataFrame(df.dtypes,
        columns=['Data Type'])

print(data_types)

missing_data_counts = pd.DataFrame(df.isnull().sum(), columns=['Missing Values'])
print(missing_data_counts)

present_data_counts = pd.DataFrame(df.count(), columns=['Present Values'])
print(present_data_counts)

uniquer_values_counts = pd.DataFrame(columns=['Unique Values'])

for v in list(df.columns.values):
    uniquer_values_counts.loc[v] = [df[v].nunique()]
print(uniquer_values_counts)

minimum_values = pd.DataFrame(columns=['Minimum Values'])

for v in list(df.columns.values):
    minimum_values.loc[v] = [df[v].min()]
print(minimum_values)

maximum_values = pd.DataFrame(
        columns=['Maximum Values'])
for v in list(df.columns.values):
        maximum_values.loc[v] = [df[v].max()]
print(maximum_values)

print(pd.concat([present_data_counts, missing_data_counts, uniquer_values_counts, minimum_values, maximum_values], axis=1))


