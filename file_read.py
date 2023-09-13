file = open("students.txt", "r")    # for read = r, for write = w, for both = r+ ; here w and r+ will remove previous data from file and add new data

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
