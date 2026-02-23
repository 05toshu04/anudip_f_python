# Product prices list
cart = [1200, 500, 1200, 3000, 800, 500]

print("Original Cart:")
print(cart)

# Remove duplicates
unique_cart = list(set(cart))

print("After removing duplicates:")
print(unique_cart)

# Total amount
total = sum(unique_cart)

print("Total =", total)

# Apply discount
if total > 5000:
    total = total - (total * 0.10)
    print("10% Discount Applied")

# Add GST 18%
gst = total * 0.18
final_amount = total + gst

print("Final Amount =", final_amount)