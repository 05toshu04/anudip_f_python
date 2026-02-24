numbers = [1,2,3,4,5]

k = int(input("Enter K: "))

k = k % len(numbers)

rotated = numbers[k:] + numbers[:k]

print("Rotated List =", rotated)