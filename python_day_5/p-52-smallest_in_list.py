numbers = [5, 8, 2, 15, 10]

smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n

print("Smallest =", smallest)