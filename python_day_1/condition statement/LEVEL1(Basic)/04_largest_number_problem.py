# Largest of Two Numbers

# Take two numbers and print the greater one.
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num1 > num2:
    print("First number is greatest.")
elif num2 > num1:
    print("Second number is greatest.")
else:
    print("Both are equal.")
