d = {"a":3,"b":1,"c":2}

sorted_items = sorted(d.items(), key=lambda x: x[1])

sorted_dict = dict(sorted_items)

print(sorted_dict)