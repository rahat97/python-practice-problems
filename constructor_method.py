class Student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


rahim = Student(101, 3.65)
'''rahim.roll = 101
rahim.gpa = 3.65'''
# rahim.set_value(101, 3.65)
rahim.display()


karim = Student(102, 3.11)
'''karim.roll = 102
karim.gpa = 3.11'''
# karim.set_value(102, 3.11)
karim.display()
