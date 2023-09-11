
numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a text of numbers: ")

for x in text:
    x = x.lower()
    if 'a' <= x <= 'z':
        numOfLetters = numOfLetters + 1

    elif '0' <= x <= '9':
        numOfDigits = numOfDigits + 1

    elif x == ' ':
        numOfWords = numOfWords + 1

print("Number of WORDS: ", numOfWords)  # numOfWords+1
print("Number of LETTERS: ", numOfLetters)
print("Number of DIGITS: ", numOfDigits)