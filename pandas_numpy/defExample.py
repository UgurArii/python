import pandas as pd
import numpy as np

df = pd.DataFrame({'Item':['TV','Mobile','Laptop'],
                   'Price': np.random.randn(3)**2*1000})
print(df)
Student = ['Ahmed','Ali','Salim','Abdullah']

def displaynames(x):
    for name in x:
        print(name)
print(displaynames(Student))

handle = open("/root/Desktop/pythonTest/country.txt")
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
print(counts)

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print("\n bigword and bigcount")
print(bigword, bigcount)
print((100,1,2) > (150,1,2))
print((0,1,120) < (0,3,4))
print (( 'Javed', 'Salwa' ) > ('Omar', 'Sam'))
print (( 'Khalid', 'Ahmed') < ('Ziad', 'Majid'))


data = {'Omar':[90,50,89],'Ali':[78,75,73],'Osama':[67,75,80]}
df1 = pd.DataFrame(data, index=['Course1','Course2','Course3'])
print(df1)
print(df1['Omar'])
df1['Mean'] = (df1['Ali'] + df1['Omar']+df1['Osama'])/3
print(df1)

