lst = [1, 2, 2, 3, 1]

result = []

for item in lst:
    if item not in result:
        result.append(item)

print(result)