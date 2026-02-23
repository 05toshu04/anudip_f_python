# Transactions list (+ deposit, - withdrawal)
transactions = [15000, -2000, 5000, -8000, 25000, -12000, 7000]

print("Transactions:")
print(transactions)

# Total balance
balance = sum(transactions)
print("Total Balance =", balance)

# Largest withdrawal
withdrawals = []

for t in transactions:
    if t < 0:
        withdrawals.append(t)

largest = min(withdrawals)

print("Largest Withdrawal =", largest)

# Deposits greater than 10000
count = 0

for t in transactions:
    if t > 10000:
        count += 1

print("Deposits >10000 =", count)