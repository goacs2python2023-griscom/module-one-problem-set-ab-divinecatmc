import math

# This program calculates the area of a circle from a radius. It's straightforward.

def area():

    radius = float(input("Enter radius: "))

    ar = radius * radius * math.pi

    print("The area of a circle with radius "+ str(radius) + " is approximately " + str(round(ar, 3) + "."))

area()