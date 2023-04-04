import matplotlib.pyplot as plt
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior',
        'Junior']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
        columns=['Names', 'Grades'])
df.plot(kind='bar')

df2 = df.set_index(df['Names'])
df2.plot(kind='bar')

df3 = pd.DataFrame(data=GradeList, columns=['Names','Grades','Gender'])
df3.boxplot(column='Grades')