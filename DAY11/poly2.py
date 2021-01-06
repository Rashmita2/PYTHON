#Polymerphism- Operator overloading

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add(self,other):
        m1 = self.m1 + other.m2
        m2 = self.m2 + other.m1
        s3 = Student(m1,m2)

        return s3

s1 = Student(68,23)
s2 = Student(53,90)

s3 = s1 + s2
print(s3)
