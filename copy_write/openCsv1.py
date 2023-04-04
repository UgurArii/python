import datetime as dt
import csv

def fname(any):
    try:
        nm = any.split(',')
    except IndexError:
        return ''
    
# Get just the last name from full name.
def lname(any):
    try:
        nm = any.split(',')
        return nm[0]
    except IndexError:
        return ''
# Convert string to integer or zero if no value.

def data(any):
    try:
        return dt.datetime.strptime(any, "%m%d%Y").date()
    except ValueError:
        return None
# Convert any string to Boolean, False if no value.
def boolean(any):
    return bool(any)

# Convert string to float, or to zero if no value.
def floatnum(any):
    s_balance = (any.replace('$','').replace(',','')).strip()
    return float(s_balance or 0)
# Create an empty list of people.
people = []
#Create an empty list of people
class Person:
    def __init__(self, id, first_name, last_name, birth_year, date_joined, is_active, balance):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.date_joined = date_joined
        self.is_active = is_active
        self.balance = balance
# Open CSV file with UTF-8 encoding, don't read in newline characters.
with open('/root/Desktop/pythonTest/people.csv', encoding='utf-8', newline='') as f:
    # Set up a csv reader with a counter.
    reader = enumerate(csv.reader(f))
    #Skip the first row, which is column names
    f.readline()
    # Loop through remaining rows one at a time, i is counter, row is entire row
    for i, row in reader:
        # From each data row in the CSV file, create a Person object with unique
#id and appropriate data types, add to people list.
        people.append(Person(i, fname(row[0]), lname(row[0]), boolean(row[3]), floatnum(row[4])))
# When above loop is done, show all objects in the people list.
for p in people:
    print(p.id, p.first_name, p.last_name, p.birth_year, p.date_joined, p.is_active, p.balance)






















    


