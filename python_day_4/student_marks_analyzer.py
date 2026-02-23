# List of student marks
marks = [85, 90, -5, 110, 76, 88, 95, 67, 45, 102]

print("Original Marks:")
print(marks)

# Remove invalid marks
valid_marks = []

for m in marks:
    if m >= 0 and m <= 100:
        valid_marks.append(m)

print("Valid Marks:")
print(valid_marks)

# Calculate average
total = sum(valid_marks)
avg = total / len(valid_marks)

print("Average =", avg)

# Find topper
top = max(valid_marks)

print("Topper Marks =", top)

# Grade based on average
if avg >= 90:
    print("Grade = A")
elif avg >= 75:
    print("Grade = B")
elif avg >= 60:
    print("Grade = C")
else:
    print("Grade = D")