text = input("Enter string: ")

result = ""

for ch in text:

    if ch in "aeiouAEIOU":
        result = result + "*"
    else:
        result = result + ch

print(result)