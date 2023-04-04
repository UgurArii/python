import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data=GradeList,
        columns=['Names','Grades'])
print(df)
print(df['Grades'].count)
print(df['Grades'].mean)
print(df['Grades'].std)
print(df['Grades'].min)
print(df['Grades'].max)
print(df['Grades'].quantile(.25))
print(df['Grades'].quantile(.5))
print(df['Grades'].quantile(.75))

# computes the arithmetic average of a column
# mean = dividing the sum by the number of values
print(df['Grades'].mean())
# finds the median of the values in a column
# median = the middle value if they are sorted in order
print(df['Grades'].median())
# mode = the most common single value
print(df['Grades'].mode())
# computes the variance of the values in a column
print(df['Grades'].var())

print(df.var())