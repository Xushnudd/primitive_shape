from polygon import Polygon
import math

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getArea(self):
        s = (self.a + self.b + self.c)/2
        return round(math.sqrt(s*(s-self.a) * (s-self.b) * (s-self.c)), 2)
    def getPerimeter(self):
        return self.a + self.b + self.c
t = Triangle(12, 23, 34)
print(t.getArea(), t.getPerimeter())