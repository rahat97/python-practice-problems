# for lambda function
print("Lambda Function Example: ")

num = [1, 3, 4, 6, 8]

result = list(map(lambda x: x*x, num))
print(result)


# Now for comprehensive list
print("\nFor List Comprehension: ")

# [expression for item in list]
num = [1, 3, 4, 6, 8]

result = [x*x for x in num]
print(result)


# for Filter Function
print("Filter function example: ")

num = [3, 4, 5, 8, 11]

result = list(filter(lambda x: x % 2 == 0, num))
print(result)

# for comprehensive list
print("\nFor list comprehension: ")

num = [3, 4, 5, 8, 11]
result = [x for x in num if x % 2 == 0]
print(result)
