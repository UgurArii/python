import pandas as pd
import numpy as np

dataset = []
Number = [1,2,3,4,5,6,7,8,9,10]
Names = ['Ali Ahmed','Mohamed Ziad','Majid Salim','SalwaAhmed', 'Ahlam Mohamed', 'Omar Ali', 'Amna Mohammed','KhalidYousif', 'Safa Humaid', 'Amjad Tayel']
City = ['Fujairah','Dubai','Sharjah','AbuDhabi','Fujairah','Dubai', 'Sharja ', 'AbuDhabi','Sharjah','Fujairah']

columns = ['Number','Name','City']
dataset = pd.DataFrame({'Number':Number, 'Name':Names,'City': City}, columns=columns)
Gender= pd.DataFrame({'Gender':['Male','Male','Male','Female',
'Female', 'Male', 'Female', 'Male','Female', 'Male']})
Height = pd.DataFrame(np.random.randint(120,175, size=(12, 1)))
Weight = pd.DataFrame(np.random.randint(50,110, size=(12, 1)))
dataset['Gender'] = Gender
dataset['Height'] = Height
dataset['Weight'] = Weight

print(dataset.set_index('Number'))
print(dataset.describe())
print(dataset.corr())
print(dataset.groupby('City')['Gender'].count())
print(dataset.groupby('City').groups)
print(dataset.groupby(['City','Gender']).groups)
grouped = dataset.groupby('Gender')
for name, group in grouped:
    print(name)
    print(group)
    print("\n")

print(grouped.get_group('Female'))
print(grouped.agg(np.size))
print(dataset.groupby('City').filter(lambda x:len(x)>=3))
