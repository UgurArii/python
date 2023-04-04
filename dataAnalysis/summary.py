import pandas as pd
import statsmodels.formula.api as sm
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)

result = sm.ols(formula='grade ~ age + exercise + hours', data=df).fit()
print(result.summary())