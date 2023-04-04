import pandas as pd
import numpy as no

all_data = pd.DataFrame()

df = pd.read_excel("/root/Desktop/pythonTest/ds_salaries.xlsx")
all_data = all_data.append(df, ignore_index=True)

df = pd.read_excel("/root/Desktop/pythonTest/test.xlsx")
all_data = all_data.append(df, ignore_index=True)

print(all_data.describe())

import glob
all_data = pd.DataFrame()
for f in glob.glob("datasets/data*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()

