import json

url = ' http://python-data.dr-chuck.net/comments_244984.json'
print('Retrieving',url)
"""
uh = urllib.urlopen(url)
data = uh.read()"""
with open('comments.json') as json_data:
     JSONdta = json.load(json_data)
     print(JSONdta)

sumv=0
counter=0
for i in range(len(JSONdta["comments"])):
    counter+=1
    Name = JSONdta["comments"][i]["name"]
    Count = JSONdta["comments"][i]["count"]
    sumv+=int(Count)
    print (Name," ", Count)
    print ("\nCount: ", counter)
    print ("Sum: ", sumv)