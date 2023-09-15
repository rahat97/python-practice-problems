import re
pattern = r"^colo..r$"

if re.match(pattern, "colouar"):
    print("Matched")


pattern = r"(ab)*"

if re.match(pattern, "abaacolour"):
    print("Matched")


pattern = r"a+b"

if re.match(pattern, "abcolor"):
    print("Matched")


pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Matched")


pattern = r"a{1,3}$"

if re.match(pattern, "aa"):
    print("Matched")

