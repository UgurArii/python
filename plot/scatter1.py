import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(20,5),columns=['Jan','Feb','March','April','May'])
df.plot.scatter(x='Feb', y='Jan', title='Temperature over two months')




