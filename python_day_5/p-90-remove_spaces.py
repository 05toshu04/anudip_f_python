text = input("Enter string: ")

result = ""

for ch in text:
    if ch != " ":
        result = result + ch

print(result)