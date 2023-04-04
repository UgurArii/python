import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("/root/Desktop/pythonTest/NCHS.csv")
print(data.head(4))

print(data.shape)


#remove all rows with na cases
data = data.dropna()
print(data.shape)

causes = data["Race"].unique()
print(causes)

dyear = data.groupby(['Year']).sum()
print(dyear)
dyear.plot(title="Death per year \n1999-­2015")
data1 = data[data["Race"] !="United States"]
dataset2 = data1.groupby("Year").sum()
dataset2.sort_values("Race", ascending=False ,
inplace = True)
dataset2.head(10)