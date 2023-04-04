import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
ssns = ['867-53-0909','333-22-4444','123-12-1234',
        '777-93-9311','123-12-1423']
GradeList = zip(names,grades,bsdegrees,msdegrees,
        phddegrees,ssns)
columns=['Names','Grades','BS','MS','PhD',"ssn"]
df = pd.DataFrame(data = GradeList, columns=columns)
def right(s, amount):
    return s[-amount]
def standardize_ssn(ssn):
    try:
        ssn = ssn.replace("-","")
        ssn = "".join(ssn.split())
        if len(ssn)<9 and ssn != 'Missing':
            ssn="000000000" + ssn
            ssn=right(ssn,9)
    except:
        pass
    return ssn
df.ssn = df.ssn.apply(standardize_ssn)
print(df)