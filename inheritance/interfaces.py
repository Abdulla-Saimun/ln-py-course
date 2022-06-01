#using abstract Based classes to enforce class constrains

from abc import ABC, abstractclassmethod
from turtle import circle

class JSONify(ABC):
    @abstractclassmethod
    def toJSON(self):
        pass

class GraphicShape:
    def __init__(self):
        super().__init__()

    @abstractclassmethod
    def calcArea(self):
        return 'hello'

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14*self.radius**2 

    def toJSON(self):
        return f"{{ \"circle\": {str(self.calcArea())}  }}"   #conver to json

    

c1 = Circle(10)
print(c1.calcArea())
print(c1.toJSON())