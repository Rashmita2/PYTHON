#INHERITANCE
class Animal():  #base class
    def __init__(self):
        print("Animal Created")

    def whoIam(self):
        print("Animal")

    def eat(self):
        print('Eating')

#passing whole class
#can inherit the function of the Animal class as well
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def bark(self):
        print('barking')

myDog = Dog()
myDog.whoIam()
myDog.eat()
myDog.bark()
print()
myAnimal = Animal()
myAnimal.whoIam()
myAnimal.eat()
