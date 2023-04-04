import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(4,3), columns=list('bde'), index=['Utah','Ohio','Texas','Oregon'])
print(frame)
print(np.abs(frame))

f = lambda x: x.max() - x.min()
print(frame.apply(f))
print(frame.apply(f, axis='columns'))

format = lambda x: '%.2f' % x
print(frame.applymap(format))

import pandas_datareader.data as web
all_data = {ticker: web.get_data_yahoo(ticker)
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
print(all_data)