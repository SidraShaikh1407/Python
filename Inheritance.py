# Aim:WAP in python to implement Inheritance
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No:40
print("***************************")
print("Inheritence")
print("***************************")
class Person:
    name=""
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
class Teacher:
    exp=0
    r_area:""
    def __init__(self,name,age,exp,r_area):
        Person.__init__(self,name,age)
        self.exp=exp
        self.r_area=r_area
    def displayData(self):
        Person.display(self)
        print("exp: ",self.exp)
        print("r_area: ",self.r_area)
class Student:
    course=""
    marks=0
    def __init__(self,name,age,course,marks):
        Person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displayData(self):
        Person.display(self)
        print("course: ",self.course)
        print("marks: ",self.marks)
print("\n##TEACHER##\n")
T=Teacher("Ashfaque Shaikh",40,18,"JAVA")
T.displayData()
print("\n##STUDENT##\n")
S=Student("Sidra Shaikh",19,"BE",90)
S.displayData()


