class Car:

    wheels = 4
    def __init__(self):
        self.miles = 1000
        self.company = "BMW"

c1 = Car()
c2 = Car()

print('The miles is {} and company is {}'.format(c1.miles, c1.company))
print(c2.wheels)


