class Car():  
    def __init__(self, color, year):
        self.color = color
        self.year = year
ford = Car("blue", 2016)
subaru = Car("red",2018)
print(ford.color, ford.year)
print(subaru.color, subaru.year)
        