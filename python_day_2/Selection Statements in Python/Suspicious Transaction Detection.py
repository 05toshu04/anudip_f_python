amount = float(input("Enter transaction amount: "))
age = int(input("Enter account age in months: "))
international = input("Is it international transaction (yes/no): ")

if amount > 200000 and age < 6 and international == "yes":
    print("Transaction Flagged for Manual Verification")
else:
    print("Transaction is Normal")