import pandas as pd
import numpy as np
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)

def singlename(fn, ln):
    return fn + " " + ln

df['fullname'] = singlename(df['fname'], df['lname'])
print(df)