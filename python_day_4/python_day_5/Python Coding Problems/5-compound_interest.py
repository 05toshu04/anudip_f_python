p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

amount = p * (1 + r/100) ** t
ci = amount - p

print("Compound Interest =", ci)