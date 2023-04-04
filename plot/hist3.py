import pandas as pd
import numpy as np
df = pd.DataFrame({'April':np.random.rand(1000)+1,'May':np.random.randn(1000),'June':np.random.rand(1000)-1}, columns=['April','May','June'])
df.hist(bins=20)