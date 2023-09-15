import re
'''
sub(pattern, replace, string)
'''
pattern = r"colour"
text = "My favourite colour is Red. I love blue colour as well"
txt = re.sub(pattern, "color", text)
'''
txt = re.sub(pattern, "color", text, count=1) # 1st match will replace for count = 1
'''
print(txt)