import pandas as pd
a = pd.read_csv('/root/Desktop/pythonTest/ds_salaries.csv')
b = pd.read_csv('/root/Desktop/pythonTest/sales.csv')

print(a.head())
print(b.head())
print(b.drop('total_profit', axis=1, inplace=True))
columns = ['month_number','facecream']
print(b.drop(columns, inplace=True, axis=1))

dataX = a.merge(b)
print(dataX.head)
