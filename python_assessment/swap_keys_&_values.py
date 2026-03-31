d = {"a": 1, "b": 2}

swapped = {}

for key in d:
    value = d[key]
    swapped[value] = key

print(swapped)