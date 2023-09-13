file = open("students.txt", "r")

# print(file.readable())
'''text = file.read()
print(text)'''     # read file

# lengths of text from file
'''size = len(text)    
print(size)'''

# each line print or as a list print each line from file.
'''text = file.readlines()    
print(text)'''

# list print with index no from file
'''text = file.readlines()[1]  
print(text)'''

# using for loop
for line in file:
    print(line)


file.close()
