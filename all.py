import math


def cylinder_csa(r, h):
    return 2 * math.pi * r * h

def cylinder_tsa(r, h):
    return 2 * math.pi * r * (r + h)

def cylinder_volume(r, h):
    return math.pi * r * r * h



def cone_csa(r, l):
    return math.pi * r * l

def cone_tsa(r, l):
    return math.pi * r * (r + l)

def cone_volume(r, h):
    return (1/3) * math.pi * r * r * h



def cuboid_lsa(l, b, h):
    return 2 * h * (l + b)

def cuboid_tsa(l, b, h):
    return 2 * (l*b + b*h + h*l)

def cuboid_volume(l, b, h):
    return l * b * h



print("1. Cylinder")
print("2. Cone")
print("3. Cuboid")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))

    print("CSA =", cylinder_csa(r,h))
    print("TSA =", cylinder_tsa(r,h))
    print("Volume =", cylinder_volume(r,h))


elif choice == 2:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))

    l = math.sqrt(r*r + h*h)

    print("CSA =", cone_csa(r,l))
    print("TSA =", cone_tsa(r,l))
    print("Volume =", cone_volume(r,h))


elif choice == 3:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    h = float(input("Enter height: "))

    print("CSA =", cuboid_lsa(l,b,h))
    print("TSA =", cuboid_tsa(l,b,h))
    print("Volume =", cuboid_volume(l,b,h))

else:
    print("Invalid Choice")