text = input("Enter sentence: ")

words = text.split()

result = ""

for w in words:
    result = result + w[0].upper() + w[1:].lower() + " "

print(result)