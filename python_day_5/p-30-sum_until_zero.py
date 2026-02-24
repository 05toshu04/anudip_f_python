sum = 0

num = int(input("Enter number (0 to stop): "))

while num != 0:
    sum = sum + num
    num = int(input("Enter number (0 to stop): "))

print("Sum =", sum)