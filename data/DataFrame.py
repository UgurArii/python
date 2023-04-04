#!/usr/bin/env pythonr  
import requests
import random
import pandas as pd
r = requests.get("https://api.github.com/search/repositories?q=language:python")

data = r.json()
print(data["total_count"])


random.seed(3)

names = ["Jess", "Jordan", "Sandy", "Ted", "Barney", "Tyler",
"Rebecca"]
ages = [random.randint(18, 35) for x in range(len(names))]
people = {"names":names, "ages":ages}
df = pd.DataFrame.from_dict(people)
print(df)

print(df["ages"])
print(df["ages"][3])
print(df.loc[0]["names"])
print(df[2:5])
print(df.head())
print(df.tail(3))

header = df.keys()
print(header)

print(df.describe())

df = df.sort_values("ages")
print(df)
"""
can_drink = df[df["ages"] > 21]
print(can_drink())
"""
random.seed(321)
tenure =[random.randint(0,10)for x in range(len(df))]
df["tenure"] = tenure
print(df.head())

def ageGroup(age):
    return "Teenager" if age < 21 else "Adult"
df["age_group"] = df["ages"].apply(ageGroup)
print(df.head(10))
print(df.groupby("age_group", as_index=False).count().head())
print(df.groupby(["age_group","tenure"], as_index=False).count().head(10))
df.loc[7] = [25,"Jess",2, "Adult"]
print(df.head(10))

df = df.drop_duplicates(subset="names")
print(df.head(10))


ratings = {"names":["Jess","Tyle","Ted"],
           "ratings":[10,9,6]
           }
print("Ratings-------")
ratings = df.from_dict(ratings)
print(ratings.head())


print("Merge Inner-------")
matched_ratings = df.merge(ratings, on="names", how="inner")
print(matched_ratings.head())

print("Merge Outer-------")
all_ratings = df.merge(ratings, on="names", how="outer")
print(all_ratings.head())























