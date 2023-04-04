import pandas as pd
import numpy as np

salesMen = ['Ahmed', 'Omar', 'Ali', 'Ziad', 'Salwa', 'Lila']
Mobile_Sales = [2540, 1370, 1320, 2000, 2100, 2150]
TV_Sales = [2200, 1900, 2150, 1850, 1770, 2000]
df = pd.DataFrame()
df['Name'] = salesMen
df['Mobile_Sales'] = Mobile_Sales
df['TV_Sales'] = TV_Sales

df.set_index("Name",drop=True,inplace=True)
print(df)
