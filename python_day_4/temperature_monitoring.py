# Daily temperatures
temp = [35, 42, 38, 46, 40, 44, 47, 39]

print("Temperatures:")
print(temp)

# Hottest and coldest
print("Hottest =", max(temp))
print("Coldest =", min(temp))

# Count extreme days (>40)
count = 0
for t in temp:
    if t > 40:
        count += 1

print("Extreme Days =", count)

# Replace above 45 with Heat Alert
for i in range(len(temp)):
    if temp[i] > 45:
        temp[i] = "Heat Alert"

print("Updated List:")
print(temp)