import pandas as pd
import numpy as np
Location = "/root/Desktop/pythonTest/gradedata.csv"

df = pd.read_csv(Location)
print(df.tail())
print(df.take(np.random.permutation(len(df))[:100]))