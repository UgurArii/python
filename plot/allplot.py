import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import spearmanr

dataset = pd.read_csv("/root/Desktop/pythonTest/salaries.csv")
rank = dataset['rank']
discipline = dataset['discipline']
phd = dataset['phd']
service = dataset['service']
sex = dataset['sex']
salary = dataset['salary']
print(dataset.head())
"""
dataset[["rank", "discipline", "phd", "service", "sex", "salary"]].plot()
dataset[["phd", "service"]].plot()

dataset1 = dataset.groupby(['service']).sum()
dataset1.sort_values("salary", ascending=False,
                     inplace=True)
print(dataset1.head())
"""
#sns.swarmplot(x='sex', y='salary', hue='rank',data=dataset, palette="Set2", dodge=True)
sns.swarmplot(x='sex',y='salary', data=dataset, hue='rank', palette="Set2",dodge=False)
sns.jointplot(x='salary', y='service', data=dataset, kind='reg')
sns.jointplot(x='salary', y='service', data=dataset, kind='hex')
sns.jointplot(x='salary', y='service', data=dataset, kind='kde')
#sns.jointplot('salary','service', data=dataset, stat_func = spearmanr)
sns.jointplot('salary','service', data=dataset).plot_joint(sns.kdeplot, n_levels=6).plot_marginals(sns.rugplot)

