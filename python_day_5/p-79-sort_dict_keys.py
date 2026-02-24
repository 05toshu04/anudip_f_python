d = {"c":3,"a":1,"b":2}

sorted_dict = {}

for k in sorted(d):
    sorted_dict[k] = d[k]

print(sorted_dict)