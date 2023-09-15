import re
pattern = r"colour"
if re.match(pattern, "Red is color, I love red colour"):
    print("Matched")
else:
    print("Not Matched")


if re.search(pattern, "Red is color, I love red colour"):
    print("Matched")
else:
    print("Not Matched")


print(re.findall(pattern, "Red is a colour, I love red colour"))



