s = input("Enter string: ")

freq = {}

# Step 1: count frequency
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Step 2: find first non-repeating
for ch in s:
    if freq[ch] == 1:
        print(ch)
        break