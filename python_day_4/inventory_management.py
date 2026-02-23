# Product stock list
stock = [0, 5, 20, 8, 0, 15, 3, 12]

print("Original Stock:")
print(stock)

# Remove zero stock
new_stock = []

for s in stock:
    if s != 0:
        new_stock.append(s)

# Restock items below 10
for i in range(len(new_stock)):
    if new_stock[i] < 10:
        new_stock[i] = new_stock[i] + 50

print("Updated Stock:")
print(new_stock)

# Total inventory
total = sum(new_stock)

print("Total Inventory =", total)