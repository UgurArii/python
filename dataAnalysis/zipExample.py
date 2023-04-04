import pandas as pd
names = ['Bob','Jessi','Mary','John','Mel','Sam',
        'Cathy','Hank','Lloyd']
grades = [76,95,77,78,99,84,79,100,73]
bsdegrees = [1,1,0,0,1,1,1,0,1]
msdegrees = [2,1,0,0,0,1,1,0,0]
phddegrees = [0,1,0,0,0,2,1,0,0]
GradeList = zip(names,grades,bsdegrees,msdegrees,
        phddegrees)

df = pd.DataFrame(data = GradeList, columns=['Name','Grade','BS','MS','PhD'])
print(df)