import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set(style='white', color_codes=True)

dataset = pd.read_csv('/root/Desktop/pythonTest/NCH.csv', index_col=0)
print(dataset.shape)
dataset.index.name = 'Index'
dataset.columns = map(str.capitalize, dataset.columns)
print(dataset.head(2))

dataset_Gun = dataset
print(dataset_Gun.Sex.value_counts(normalize=False))

dataset_byGender = dataset_Gun.groupby('Sex').count()
print(dataset_byGender)


dataset_suicide_Gender =dataset_Gun[
dataset_Gun["Intent"] =="Suicide"]
dataset_suicide_Gender.Sex.value_counts(normalize=False).plot.bar(title='Annual U.S.\\suicide gun deaths \n 2012-2014, by gender')
dataset_byGender.plot.bar(title='Annual U.S. suicidegun deaths \n 2012-2014, by gender')




