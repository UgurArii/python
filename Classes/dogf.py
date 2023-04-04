class Dog():
    name=''
    def setName(self, new_name):
        self.name = new_name
    def getName(self):
        return self.name
sam = Dog()
sam.setName("Sammi")
print(sam.getName())

class Dog1():
    age = 5
    def happyBirthday(self):
        self.age += 1
sam = Dog1()
sam.happyBirthday()
print(sam.age)
sam.happyBirthday()
print(sam.age)


class Dog2():
    age=6
    def getAge(self):
        return self.age
    def printInfo(self):
        if self.getAge() <10:
            print("Puppy!")
sam = Dog2()
sam.printInfo()

class Dog4():
    def __str__(self):
        return "This is a dog class"
sam = Dog()
print(sam)


class Animal():
    def _init__(self, species):
        self.species = species
class Dog(Animal):
    def __init__(self, species, name):
        self.name = name
        super().__init__(species)
sam = Dog("Canine","Sammi")
print(sam.species)

#interigin Multiple Classes
class Physics():
    gravity = 9.8
class Automobile():
    def __init__(self, make, model, year):
        self.make, self.model, self.year = make, model, year

class Ford(Physics, Automobile):
    def __init__(self, model, year):
        Automobile("Ford", model, year)
truck = Ford("F-150",2018)
print(truck.gravity, truck.make)
























