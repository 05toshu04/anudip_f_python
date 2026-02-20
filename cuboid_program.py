import three_figures as tf

l = float(input("Enter Length: "))
b = float(input("Enter Breadth: "))
h = float(input("Enter Height: "))

print("Curved Surface Area =", tf.cuboid_lsa(l,b,h))
print("Total Surface Area =", tf.cuboid_tsa(l,b,h))
print("Volume =", tf.cuboid_volume(l,b,h))