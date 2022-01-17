import math

ab = int(input())
bc = int(input())
x = ab ** 2
y = bc ** 2

ca = ((x + y) ** (1/2)) 

acb = round((math.acos(bc / ca) * 180 / math.pi))

print(f"{acb}" + "°")

