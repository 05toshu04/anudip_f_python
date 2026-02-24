t = (1,2,3,4,5)

unique = True

for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i] == t[j]:
            unique = False

if unique:
    print("All Elements Unique")
else:
    print("Duplicate Elements Found")