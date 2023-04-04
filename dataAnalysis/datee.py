import pandas as pd
from time import strftime
from datetime import datetime
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
bdates = ['1/1/1945','10/21/76','3/3/90',
        '04/30/1901','1963-09-01']
GradeList = zip(names,grades,bsdegrees,msdegrees,
        phddegrees,bdates)
columns=['Names','Grades','BS','MS','PhD',"bdates"]
df = pd.DataFrame(data = GradeList, columns=columns)
print(df)

def standardize_date(the_date):
    formatted_date = ""
    thedate = str(thedate)
    if not the_date or the_date.lower() == "missing" or thedate == "nan":
        formatted_date = "MISSING"
    if the_date.lower().find('x') != -1:
        formatted_date = "Incomplete"
    if the_date[0:2] == "00":
        formatted_date = thedate.replace("00", "19")
    try:
        formatted_date = str(datetime.strptime(the_date, '%m/%d/%y').strftime('%m/%d/%y'))
    except:
        pass
    try:
        formatted_date = str(datetime.strptime(thedate, '%m/%d/%Y').strftime('%m/%d/%y'))
    except:
        pass
    try:
        if int(the_date[0:4])<1900:
            formatted_date = "Incomplete"
        else:
            formatted_date = str(datetime.strptime(the_date, '%Y-%m-%d').strftime('%m/%d/%y'))
    except:
        pass
    return formatted_date
df.bdates = df.bdates.apply(standardize_date)
print(df)