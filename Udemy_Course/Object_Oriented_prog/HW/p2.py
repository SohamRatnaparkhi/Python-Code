class Cylinder:
    pi = 3.14
    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        v = Cylinder.pi * (self.radius ** 2) * self.height
        return v

    def surface_area(self):
        s = Cylinder.pi * (self.radius * 2) * self.height
        return s

mycylinder = Cylinder(2,3)


print(f"Surface area: {mycylinder.surface_area()}")
print(f"Volume: {mycylinder.volume()}")