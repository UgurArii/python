import pandas as pd
names = ['Jan','John','Bob','Jan','Mary','Jon','Mel','Mel']
grades = [95,78,76,95,77,78,99,100]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
        columns=['Names', 'Grades'])
print(df)

print(df.duplicated())
print(df.drop_duplicates())
print(df.drop_duplicates(['Names'], keep='last'))