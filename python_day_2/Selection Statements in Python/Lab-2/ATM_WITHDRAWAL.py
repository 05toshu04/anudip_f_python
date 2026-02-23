balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM cash available: "))

if withdraw > balance:
    print("Insufficient Balance")
elif withdraw > 50000:
    print("Daily Limit Exceeded")
elif withdraw > atm_cash:
    print("ATM has insufficient cash")
else:
    balance -= withdraw
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)
