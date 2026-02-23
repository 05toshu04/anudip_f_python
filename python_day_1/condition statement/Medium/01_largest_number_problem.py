# 6️⃣ Largest of Three Numbers

# Take three numbers and print the largest.
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if num1 > num2:
    if num1 > num3:
        print("First number is greatest")

    else:
        print("Third number is greatest")
elif num2 > num1:
    # print("Second number is greatest")

    if num2 > num3:
        print("Second number is greatest.")
    else:
        print("Third number is greatest")

else:
    print("All numbers are equal")
