marks = {
    "Amit": 85,
    "Ravi": 92,
    "Sita": 88,
    "Neha": 95
}

topper = max(marks, key=marks.get)

print("Topper =", topper)
print("Marks =", marks[topper])