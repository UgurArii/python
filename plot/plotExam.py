import pandas as pd
import seaborn as sns
import numpy as np
dataset = pd.read_csv("/root/Desktop/pythonTest/salaries.csv")
rank = dataset['rank']
discipline = dataset['discipline']
phd = dataset['phd']
service = dataset['service']
sex = dataset['sex']
salary = dataset['salary']
print(dataset.head())

dataset[["rank", "discipline", "phd", "service", "sex", "salary"]].plot()
dataset[["phd", "service"]].plot()

dataset1 = dataset.groupby(['service']).sum()
dataset1.sort_values("salary", ascending=False,
                     inplace=True)
print(dataset1.head())

dataset1["salary"].plot.bar()
dataset[['phd', 'service']].head(10).plot.bar()
dataset[['phd','service']].head(10).plot.bar(title="PHD Vs Servise\n2018")
dataset[['phd','service']].head(10).plot.bar(title="PHD Vs Servise\n2018", color=['g','red'])
dataset["salary"].head(10).plot.pie(autopct='%.2f')
dataset[['phd','salary']].head(100).plot.box()
dataset[['phd','service']].plot.box()
dataset['salary'].head(20).plot.hist()
dataset.plot(kind='scatter', x='phd',y='service',title='Popuation vs area and density\n 2018', s=0.9)
sns.stripplot(x=dataset['salary'])
sns.stripplot(x=dataset['sex'],y=dataset['salary'], data=dataset)
sns.stripplot(x=dataset['discipline'], y=dataset['salary'], data=dataset, jitter=1)
sns.stripplot( x= dataset['salary'], y = dataset['discipline'],
data=dataset, jitter=True)
sns.stripplot(x='sex', y='salary', hue='rank', data=dataset, jitter=True)
sns.boxplot(x='salary', y='sex', data=dataset, whis=np.inf)
sns.stripplot(x = 'salary', y ='sex', data=dataset,
jitter=True, color='0.02')
sns.boxplot(x = dataset['salary'])
sns.boxplot(x=dataset['salary'], notch=True)
sns.boxplot(x = dataset['salary'], whis=2)
sns.boxplot(x='rank', y='salary', data=dataset)
sns.boxplot(x = 'rank', y = 'salary', hue='sex', data=dataset,
palette='Set3')
sns.boxplot(x = 'rank', y = 'salary', data=dataset)
sns.swarmplot(x = 'rank', y = 'salary', data=dataset,
color='0.25')