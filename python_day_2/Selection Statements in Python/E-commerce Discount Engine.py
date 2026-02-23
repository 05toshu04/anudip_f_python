cart = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Is it festival season (yes/no): ")

d1 = d2 = 0

if membership == "Silver":
    d1 = 0.05
elif membership == "Gold":
    d1 = 0.10
elif membership == "Platinum":
    d1 = 0.15

if festival == "yes":
    d2 = 0.10

final_discount = max(d1, d2)
payable = cart - (cart * final_discount)

print("Final Payable Amount:", payable)