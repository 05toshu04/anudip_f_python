# Ratings list
ratings = [5, 4, 3, 6, 2, 5, 1, 0, 4]

print("Original Ratings:")
print(ratings)

# Remove invalid ratings
valid = []

for r in ratings:
    if r >= 1 and r <= 5:
        valid.append(r)

print("Valid Ratings:")
print(valid)

# Average rating
avg = sum(valid) / len(valid)
print("Average =", avg)

# Count 5 star ratings
count = valid.count(5)

print("5 Star Ratings =", count)

# Sort ascending
valid.sort()

print("Sorted Ratings:")
print(valid)