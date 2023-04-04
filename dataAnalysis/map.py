import pandas as pd
import numpy as np
Location = "/root/Desktop/pythonTest/gradedata.csv"

df = pd.read_csv(Location)

df.columns = map(str.lower, df.columns)
print(df.columns)
df.columns = [x.lower() for x in df.columns]