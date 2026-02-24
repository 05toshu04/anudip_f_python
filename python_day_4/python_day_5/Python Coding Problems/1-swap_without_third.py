# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swap:")
print("a =", a)
print("b =", b)

# Swap without third variable
a = a + b
b = a - b
a = a - b

print("After Swap:")
print("a =", a)
print("b =", b)