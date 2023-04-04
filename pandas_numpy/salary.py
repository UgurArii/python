import pandas as pd

sales = pd.read_csv('/root/Desktop/pythonTest/sales.csv')
print ("\n\n<<<<<<< First 5 records <<<<<<<\n\n")
print(sales.head())
print(sales.tail())

salesNrows = pd.read_csv('/root/Desktop/pythonTest/sales.csv', nrows=4, usecols=[0,1,6])
print(salesNrows)

salesNrowss = pd.read_csv('/root/Desktop/pythonTest/sales.csv', nrows=4, usecols=['month_number','toothpaste'])
print(salesNrowss)


print(salesNrowss.rename(columns={'month_number':'Month'}))

sales_exam = pd.read_csv('/root/Desktop/pythonTest/sales.csv', nrows=15, na_values=["NaN","not available"])
mydata = sales_exam.head(15)
print(mydata)




