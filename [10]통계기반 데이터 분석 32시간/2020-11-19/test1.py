# class
def test():
    return 'test'

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def gotoSchool(self):
        print(self.name, ', ', self.age)

stu = Student('홍길동', 30)
stu.gotoSchool()

class Employee:
    EmpName = '이순신'
    EmpAge = 300
    def working(self):
        print(self.EmpName, ", ", self.EmpAge)

emp = Employee()
emp.working()
del emp

class Animal:     
    def breath(self):
        print("Animal breath")
    def bark(self):
        print("Animal bark")

class Dog(Animal):
    def bark(self):
        print("Dog bark")

dg = Dog()
dg.breath()
dg.bark()

