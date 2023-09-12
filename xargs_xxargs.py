#xargs
print("===## xargs: ##===\n")
print("Example-01 ::")


def student(*details):      #it works like tuples
    print(details)


student(101, "Rahat")
student(101, "Rahat", 2.95)


print("\nExample-02 ::")


def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)


add(12, 22)
add(12, 22, 78)
add(12, 22, 34, 56)


print("\n\n===## xxargs: ##===\n")
print("Example-01 ::")


def student(**details):     #it works like dictionaries
    print(details)


student(id=102, name="Rahat")
