numbers = [1,2,3,2,4,5,1]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)