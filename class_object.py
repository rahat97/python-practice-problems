class student:
    roll = ""
    gpa = ""


rahim = student()
print(isinstance(rahim, student))

rahim.roll = 101
rahim.gpa = 3.7
print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")

karim = student()
print(isinstance(karim, student))

karim.roll = 102
karim.gpa = 2.9
print(f"Roll : {karim.roll}, GPA : {karim.gpa}")