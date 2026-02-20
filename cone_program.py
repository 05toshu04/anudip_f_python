import three_figures as tf
import math

r = float(input("Enter Radius: "))
h = float(input("Enter Height: "))

l = math.sqrt(r*r + h*h)

print("Curved Surface Area =", tf.cone_csa(r,l))
print("Total Surface Area =", tf.cone_tsa(r,l))
print("Volume =", tf.cone_volume(r,h))