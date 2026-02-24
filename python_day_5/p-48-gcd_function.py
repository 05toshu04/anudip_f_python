def gcd(a, b):

    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD =", gcd(x, y))