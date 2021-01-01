class Computer:
    def __init__(self):
        self.name = "Tim"
        self.age = 30
    
    def update(self):
        self.age = 35

    def compare(self, other):
        #here c1 becomes self and c2 becomes other
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
#can change the name and age of c1 or c2
c1.name = "Jerry"
c2 = Computer()
c1.update()
print(c1.name)
print(c2.name)
print(c1.age)

#to compare c1 and c2
if c1.compare(c2):
    print("They are same")
else:
    print('They are different')