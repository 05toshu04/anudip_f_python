text = input("Enter a string: ")

rev = ""

for ch in text:
    rev = ch + rev

print("Reverse =", rev)