text = input("Enter string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch,0) + 1

print(freq)