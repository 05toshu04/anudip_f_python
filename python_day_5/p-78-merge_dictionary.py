dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}

merged = {}

for k in dict1:
    merged[k] = dict1[k]

for k in dict2:
    merged[k] = dict2[k]

print(merged)