# Student scores list
scores = [25, 32, 34, 45, 60, 38, 29, 80]

print("Original Scores:")
print(scores)

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

print("After removing lowest 2:")
print(scores)

# Add grace marks
for i in range(len(scores)):
    if scores[i] >= 30 and scores[i] <= 35:
        scores[i] = scores[i] + 5

print("After Grace Marks:")
print(scores)

# Count passed students
count = 0

for s in scores:
    if s >= 40:
        count += 1

print("Passed Students =", count)