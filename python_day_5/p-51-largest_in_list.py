numbers = [5, 8, 2, 15, 10]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest =", largest)