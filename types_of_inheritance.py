# Multi-level inheritance
class A:
    def display1(self):
        print("I'm inside class A")


class B(A):
    def display2(self):
        print("I'm inside class B")


class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I'm inside class C")


obj1 = C()
obj1.display3()


# Multiple inheritance
class A:
    def display(self):
        print("I'm inside class A")


class B:
    def display(self):
        print("I'm inside class B")


class C(A, B):
    pass
    '''def display3(self):
        print("I'm inside class C")'''


obj1 = C()
obj1.display()

