import pandas as pd 
import numpy as np

df = pd.DataFrame(np.random.randn(200,6), index=pd.date_range('1/9/2009',periods=200), columns=list('ABCDEF'))
df.plot(figsize=(20, 10)).legend(bbox_to_anchor=(1, 1))