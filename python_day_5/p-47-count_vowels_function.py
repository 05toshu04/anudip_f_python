def count_vowels(text):

    count = 0

    for ch in text:
        if ch in "aeiouAEIOU":
            count += 1

    return count

text = input("Enter string: ")
print("Vowels =", count_vowels(text))