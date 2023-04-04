import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April','May'])
df.plot.hist(bins=40, figsize=(10,8)).legend(bbox_to_anchor=(1.2,1))