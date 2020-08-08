from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0

class Rectangle(shape):
    type = "Rectangle"

    def __init__(self):
        self.len = 3
        self.brd = 4


    def printArea(self):
        return self.len * self.brd

rec1 = Rectangle()
print(rec1.printArea())

