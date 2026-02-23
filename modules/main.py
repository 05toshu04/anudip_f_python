import three_figures as tf
import math

print("CYLINDER")
r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area =", tf.cylinder_csa(r,h))
print("Total Surface Area =", tf.cylinder_tsa(r,h))
print("Volume =", tf.cylinder_volume(r,h))

print("\nCONE")
r = float(input("Enter radius: "))
h = float(input("Enter height: "))

l = math.sqrt(r*r + h*h)

print("Curved Surface Area =", tf.cone_csa(r,l))
print("Total Surface Area =", tf.cone_tsa(r,l))
print("Volume =", tf.cone_volume(r,h))

print("\nCUBOID")
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

print("Curved Surface Area =", tf.cuboid_lsa(l,b,h))
print("Total Surface Area =", tf.cuboid_tsa(l,b,h))
print("Volume =", tf.cuboid_volume(l,b,h))