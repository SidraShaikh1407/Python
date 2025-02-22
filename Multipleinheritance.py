# Aim: Write a Program in python to implement Multiple Inheritence.
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No:40
print("***************************")
print("Multiple Inheritence")
print("***************************")
class Employee:
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id      
        self.emp_name = emp_name  
    def set_emp_id(self, emp_id):
        self.emp_id = emp_id
    def get_emp_id(self):
        return self.emp_id
    def set_emp_name(self, emp_name):
        self.emp_name = emp_name
    def get_emp_name(self):
        return self.emp_name
class Student:
    def __init__(self, student_id, student_name, student_college):
        self.student_id = student_id      
        self.student_name = student_name  
        self.student_college = student_college
    def set_student_id(self, student_id):
        self.student_id = student_id
    def get_student_id(self):
        return self.student_id
    def set_student_name(self, student_name):
        self.student_name = student_name
    def get_student_name(self):
        return self.student_name
    def set_student_college(self, student_college):
        self.student_college = student_college
    def get_student_college(self):
        return self.student_college
class Intern(Employee, Student):
    def __init__(self, emp_id, emp_name, student_id, student_name, student_college, period):
        Employee.__init__(self, emp_id, emp_name)  
        Student.__init__(self, student_id, student_name, student_college)  
        self.period = period  
    def set_period(self, period):
        self.period = period
    def get_period(self):
        return self.period
    def display_intern_details(self):
        print(f"Employee ID: {self.get_emp_id()}")
        print(f"Employee Name: {self.get_emp_name()}")
        print(f"Student ID: {self.get_student_id()}")
        print(f"Student Name: {self.get_student_name()}")
        print(f"Student College: {self.get_student_college()}")
        print(f"Internship period: {self.get_period()} months")
intern = Intern(emp_id="5678", emp_name="Sana Shaikh", student_id="231P064", student_name="Sidra Shaikh", student_college="RCOE", period=6)
intern.display_intern_details()
