text = input("Enter string: ")

rev = text[::-1]

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")