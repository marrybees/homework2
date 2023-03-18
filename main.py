class Rectangle:
    def __init__(self,width,length,color):
        self.width = width
        self.length = length
        self.color = color

    def perimeter(self):
         return 2 * (self.width + self.length)
    def area(self):

        return self.length * self.width

obj1 = Rectangle(5,1,"blue")
obj2 = Rectangle(3,3,"green")
obj3 = Rectangle(7,3,"purple")

print(obj1.area())
print(obj1.perimeter())
print(obj2.area())
print(obj2.perimeter())
print(obj3.perimeter())
print(obj3.area())

#homework2
class Car:
    def __init__(self,brendi,modeli,feri):
        self.brendi = brendi
        self.modeli = modeli
        self.feri = feri

    def __str__(self):
        return f"manqanis brendia {self.brendi},modelia {self.modeli},feria {self.feri}"

car1 = Car("ford","mustang","witeli")
car2 = Car("toiota","prius","lurji")
car3 = Car("volksvagen","golf","mwvane")
print(car1)
print(car2)
print(car3)
#homework3
class Dog:
    def __init__(self,breed,size,age,color):
        self.breed = breed
        self.size = size
        self.color = color
        self.age = age
    def eat (self):
        return "sachmeli"
    def run (self):
        return "4 km/st"
    def age (self):
        return "3"
    def sit (self):
        return "dajda"
    def __str__(self):
        return f"dzaghlis jishia{self.breed},zoma {self.size},asakia{self.age},feria{self.color}"

dog1 = Dog("neapolitan mastif","large","5 years","black")
dog2 = Dog("maltese","small","2 years","white")
dog3 = Dog("chow chpw","midium","3 years","brown")
print(dog1)
print(dog2)
print(dog3)
print(dog1.run())
