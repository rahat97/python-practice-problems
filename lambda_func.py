# first as normal function or named function

def calculate(a,b):
    return a*a + 2*a*b + b*b


print("Result =", calculate(3,4))

#now, same function as a Lambda function

# lambda parameter : expression

calculate = (lambda a, b: a*a + 2*a*b + b*b)(3, 4)

print("Lambda function Result: ", calculate)
