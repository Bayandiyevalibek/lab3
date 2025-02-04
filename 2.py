class Shape:
    def area(self):
        return 0

class Square:
    def __init__(self,length):
        self.lenght = length
    def area(self):
        return self.lenght ** 2
    
shape = Shape()
square = Square(5)

print(shape.area())
print(square.area())
