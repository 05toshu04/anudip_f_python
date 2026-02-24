def palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

text = input("Enter string: ")
print(palindrome(text))