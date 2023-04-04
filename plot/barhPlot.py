import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April','May'])

df.plot.barh(stacked=True,figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))
