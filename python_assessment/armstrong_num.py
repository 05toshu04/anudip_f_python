n = int(input("Enter number: "))
temp = n
digits = len(str(n))

sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

print(sum == n)