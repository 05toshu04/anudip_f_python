list1 = [1,2,3,4]
list2 = [3,4,5,6]

merged = list1 + list2

unique = []

for n in merged:
    if n not in unique:
        unique.append(n)

print(unique)