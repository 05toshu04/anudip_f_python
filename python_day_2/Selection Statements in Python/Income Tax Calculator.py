income = float(input("Enter your income: "))
age = int(input("Enter your age: "))

if age >= 60:
    exemption = 300000
else:
    exemption = 250000

if income <= exemption:
    tax = 0
elif income <= 500000:
    tax = (income - exemption) * 0.05
elif income <= 1000000:
    tax = (income - exemption) * 0.20
else:
    tax = (income - exemption) * 0.30

print("Tax to be paid:", tax)