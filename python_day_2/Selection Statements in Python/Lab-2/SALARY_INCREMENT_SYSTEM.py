rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance %: "))

increment = 0

if rating >= 4:
    increment += 10
elif rating == 3:
    increment += 5

if experience >= 5:
    increment += 5

if attendance >= 90:
    increment += 3

print("Increment % =", increment)
