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


# more on search function

pattern = r"colour"
text = "My favourite colour is Red"
match = re.search(pattern, text)

if match:
    print(match.start())
    print(match.end())
    print(match.span())




