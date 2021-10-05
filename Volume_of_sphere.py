import math

radius = input("Enter Radius: ")
print("Radius: " + str(radius))

r = float(radius)

volume = 4.0/3.0 * math.pi * (r*r*r)
print("Volume: " + str(round(volume,2)))
