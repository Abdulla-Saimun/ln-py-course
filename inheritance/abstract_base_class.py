#using abstract Based classes to enforce class constrains

from abc import ABC, abstractclassmethod
from turtle import circle

class GraphicShape:
    def __init__(self):
        super().__init__()

    def calcArea(self):
        return 'hello'

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    def calcArea(self):
        return 3.14*self.radius**2 


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    def calcArea(self):
        return self.side*self.side


g = GraphicShape()
print(g.calcArea)
c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
