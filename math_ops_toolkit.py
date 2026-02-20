def add(a, b):
    return a + b


def difference(a, b):
    return a - b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = add(num1, num2)
diff_result = difference(num1, num2)

print("Addition = ", sum_result)
print("Difference = ", diff_result)