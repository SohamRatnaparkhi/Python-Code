class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        (x1, y1) = self.coor1
        (x2, y2) = self.coor2
        d = ((y2 - y1) ** 2 + (x1 - x2) ** 2)**0.5
        return d
    def slope(self):
        (x1, y1) = self.coor1
        (x2, y2) = self.coor2
        m = abs((y2 - y1) / (x1 - x2))
        return (m)
myline = Line((3,2), (8,10))
print(myline.distance())
print(myline.slope())