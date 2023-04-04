import pandas as pd
import matplotlib.pyplot as plt
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
        columns=['Names', 'Grades'])

df.plot()
displayText = "my annotation"
xloc = 1
yloc = df['Grades'].max()
xtext = 8
ytext = -150
plt.annotate(displayText, xy=(xloc, yloc), arrowprops=dict(facecolor='black',shrink=0.05),
             xytext=(xtext, ytext), xycoords = ('axes fraction','data'), textcoords='offset points')
