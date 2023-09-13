file = open("students.txt", "a")   # for add new data with previous data = a (append)

file.write("\nSaddam Hossain - Lecturer of Mathematics")


file = open("student01.txt", "a")   # create new text file and add data together
file.write("\nJohn Wick - Assassin")

file = open("hello.html", "w")
file.write("<h1>Hello!! This is sample text</h1>")



file.close()