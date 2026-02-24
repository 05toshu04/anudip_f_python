d = {"A":10,"B":25,"C":15}

max_key = max(d, key=d.get)

print("Key with maximum value =", max_key)
print("Value =", d[max_key])