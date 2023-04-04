import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names, grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
writer = pd.ExcelWriter('dataframe.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

