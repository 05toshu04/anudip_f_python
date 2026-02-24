text = input("Enter string: ")

rev = ""

for ch in text:
    rev = ch + rev

print("Reverse =", rev)