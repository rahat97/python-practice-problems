class student:
    roll = ""
    gpa = ""

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


rahim = student()
rahim.roll = 101
rahim.gpa = 3.7
rahim.display()


karim = student()
karim.roll = 102
karim.gpa = 2.9
karim.display()