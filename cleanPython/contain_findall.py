import pandas as pd
import numpy as np
import re
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
'Rob': 'rob@gmail.com', 'Wes': np.nan}

data = pd.Series(data)
print(data)
print(data.isnull())
print(data.str.contains('gmail'))
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
print(data.str.findall(pattern, flags=re.IGNORECASE))
matches = data.str.match(pattern, flags=re.IGNORECASE)
print(matches)
print(data.str[:5])
