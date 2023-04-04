import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

salesMen = ['Ahmed', 'Omar', 'Ali', 'Ziad', 'Salwa', 'Lila']
Mobile_Sales = [2540, 1370, 1320, 2000, 2100, 2150]
TV_Sales = [2200, 1900, 2150, 1850, 1770, 2000]
df = pd.DataFrame()
df ['Name'] =salesMen
df ['Mobile_Sales'] = Mobile_Sales
df['TV_Sales']=TV_Sales
df.plot.bar(figsize=(20,10),rot=0).legend(bbox_to_anchor=(1.1,1))
plt.xlabel('Salesman')
plt.ylabel('Sales')
plt.title('Sales Volume for two salesmen in \nJanuary and April 2017')
plt.show()
df.plot.pie(subplots=True)
df.plot.box()


