class Triangle:
    base = ""
    height = ""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Calculated Area :", area)


T1 = Triangle(10, 20)
T1.calculate_area()

T2 = Triangle(20, 30)
T2.calculate_area()
