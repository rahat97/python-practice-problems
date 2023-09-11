'''
        # Stack #
'''

print("\n===## STACK ##===")
books = []

books.append("Learn C Programming")
books.append("Learn C++ Programming")
books.append("Learn Python Programming")
books.append("Learn Java Programming")

print(books)                # for Stack always "LIFO" - Last In First Out

books.pop()
print("\nNow the TOP book is : ", books[-1])
books.pop()
print("Now the TOP book is : ", books[-1])
books.pop()
print("Now the TOP book is : ", books[-1])
books.pop()
if not books:
    print("No books Left")


'''
        # Queue #
'''
print("\n===## QUEUE ##===")

from collections import deque

bank = deque (["Rahat", "Rajib", "Karim", "Jamal"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)

bank.popleft()
if not bank:
    print("No person Left")