try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1/num2
    print(result)

except (ValueError, ZeroDivisionError):     # multiple exception error together
    print("You have entered incorrect input.")

# except ZeroDivisionError:
#    print("You can not divide a number by zero")
finally:
    print("Thanks !!")
