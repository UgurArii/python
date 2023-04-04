import pandas as pd
names = ['Nike','Adidas','New Balance','Puma','Reebok']
grades = [176,59,47,38,99]

PriceList = zip(names, grades)
df = pd.DataFrame(data = PriceList, columns=['Names','Pricess'])
print(df)