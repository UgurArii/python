import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bs = [1,1,0,0,1]
ms = [2,1,0,0,0]
phd = [0,1,0,0,0]
GradeList = zip(names,grades,bs,ms,phd)
df = pd.DataFrame(data=GradeList,
        columns=['Name','Grade','BS','MS','PhD'])
print(df)
print(df.loc[df['PhD']==0].count())