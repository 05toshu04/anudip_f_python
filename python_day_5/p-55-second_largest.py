numbers = [5,8,2,15,10]

largest = max(numbers)

second = numbers[0]

for n in numbers:
    if n != largest and n > second:
        second = n

print("Second Largest =", second)