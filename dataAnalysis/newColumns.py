import pandas as pd
import numpy as np
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
GradeList = zip(names,grades,bsdegrees,msdegrees,
        phddegrees)
columns=['Names','Grades','BS','MS','PhD']
df = pd.DataFrame(data = GradeList, columns=columns)
print(df)

print(df.drop('PhD', axis=1))
df['HighSchool']=0
df['PreSchool'] = np.nan
d = ([0,1,0,1,0])
s = pd.Series(d, index= df.index)
df['DriversLicense'] = s
print(df)