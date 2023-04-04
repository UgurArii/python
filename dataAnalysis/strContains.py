import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
        columns=['Names', 'Grades'])
print(df)
print(df['Names'].str.contains('Mel'))
print(df['Names'].str.contains('Mel').any())
print(df['Names'].str.contains('Mel').all())
print(df.loc[df['Names'].str.contains('Mel')==True])
print(df.loc[df['Grades']==0])

