class Student:
    school = "University of Texas"

    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3)/3

    #we need to use decorater called classmethod to use cls
    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This in Student class")


s1 = Student(64,79,97)
print(s1.average())
print(Student.getSchool())

Student.info()