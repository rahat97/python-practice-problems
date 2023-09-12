# Map Function
print("Map Function:")


def square(x):
    return x*x


number = [2, 4, 6, 8, 10]

result = list(map(square, number))      # map func can only receive function and iterable object
print(result)


# Filter function
print("\nFilter Function:")
'''
-filter function also worked in iterable object. here we discuss here how filter function work with lists.
-filter functions main work is to filter an object, filter function can filter an iterable object
-In a list apply a condition for filtering, if condition doesn't match in the list then, this func. remove the items from list.

'''
number = [1, 2, 3, 4, 5]


result = list(filter(lambda x: x % 2 == 0, number))
print(result)
