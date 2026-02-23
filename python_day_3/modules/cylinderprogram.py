import three_figures as tf

r = float(input("Enter Radius: "))
h = float(input("Enter Height: "))

print("Curved Surface Area =", tf.cylinder_csa(r,h))
print("Total Surface Area =", tf.cylinder_tsa(r,h))
print("Volume =", tf.cylinder_volume(r,h))