import pandas as pd
import matplotlib.pyplot as plt


names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']
df = pd.DataFrame(data=GradeList, columns=columns)
print(df)

df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']
print(df)
plt.pie(df['TotalDemerits'], labels=df['Names'],
        explode=(0.13,0.18,0.1,0.2,0.15),
        startangle=90,
        autopct='%1.1f%%')
plt.axis('equal')
plt.show()