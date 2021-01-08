class Dog():
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

myDog = Dog("lab",'rk')
otherDog = Dog('dalmation','sammy')
print(myDog.breed)
print(otherDog.name)