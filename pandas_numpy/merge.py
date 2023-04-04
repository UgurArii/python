import pandas as pd
import numpy as np

stud1 = pd.DataFrame({'ID': [1,2,3,4,5], 'names' : ['John',
'Greta', 'Francis', 'Laura', 'Charles'], 'Logic': [28, 27, 23,25, 30]})
                                                   
stud2 = pd.DataFrame({'ID': [1,6,3,4,7], 'names' : ['John',
'Kate', 'Francis', 'Laura', 'Simon'], 'Analysis': [23, 24, 28,29, 22]})
                                                   

print(pd.merge(stud1, stud2, on='ID'))
print(pd.merge(stud1, stud2, on='ID', how='left'))
print(pd.merge(stud1, stud2, on='ID', how='right'))
print(pd.merge(stud1, stud2, on='ID', how='outer'))