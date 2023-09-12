# Assign a different name to function and call it through the new name
print("Basic Problem No: 1 ::")
def display_details(id, name, age, year):
    print(id, name, age, year)

display_details( 1, "Rahat", 26, "1st")

show_student_details = display_details

show_student_details( 1, "Rahat", 26, "1st")


#Create an inner function to calculate the addition in the following way
print("\nBasic Problem No: 2 ::")
def outer_func(a, b):   #outer function
    square = a ** 2

    def addition(a,b):  #inner function
        return a + b
    add = addition(a, b)    #call inner function from outer function

    return add + 5  #add 5 to the result

result = outer_func(8, 12)
print("Result =", result)
