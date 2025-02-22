# Aim:Write a program to define a function that accepts roll numbers and returns whether thestudent is present or absent.
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No:40
print("***************************")
print("Attendance")
print("***************************")
def check_attendance(roll_number, attendance_list):
    if roll_number in attendance_list:
        return "Present"
    else:
        return "Absent"
attendance_list = [1,2,3,4,5,6,7,8,9,10,11,12,19,30,31,32,34,35,40] 
roll_number = int(input("Enter the roll number of the student: "))
status = check_attendance(roll_number, attendance_list)
print(f"The student with roll number {roll_number} is {status}.")
