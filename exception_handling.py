'''num1 = int(input("Enter a number: "))
result = 20/num1
print(result)
print("Done")'''

try:
    list = [20, 0, 30]
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index Error")
finally:
    print("Successful")

