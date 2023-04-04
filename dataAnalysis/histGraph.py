import pandas as pd
import matplotlib.pyplot as plt
Location = "/root/Desktop/pythonTest/gradedata.csv"
df = pd.read_csv(Location)

df.hist(column="hours", by="gender")