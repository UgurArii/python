import pandas as pd
import numpy as np
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)

df['isFailing'] = np.where(df['grade']<70,
'yes', 'no')
print(df.tail(10))

df['isFailingMale'] = np.where((df['grade']<70)
        & (df['gender'] == 'male'),'yes', 'no')
print(df.tail(10))