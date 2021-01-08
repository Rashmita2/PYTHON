class Circle:
    pi = 3.14
    #radius have default value of 1
    def __init__(self,radius=1):
        self.radius = radius
    
    def area(self):
        return self.radius*self.radius* Circle.pi

myc = Circle(2)
print(myc.radius)
print(myc.area())

