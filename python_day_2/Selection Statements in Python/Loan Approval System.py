credit = int(input("Enter credit score: "))
income = float(input("Enter monthly income: "))
loan = float(input("Enter existing loan amount: "))

if credit < 600:
    print("Loan Rejected")
elif credit >= 750:
    print("Loan Approved")
else:
    if income < 30000 and loan > 500000:
        print("Loan Rejected")
    else:
        print("Loan Approved")