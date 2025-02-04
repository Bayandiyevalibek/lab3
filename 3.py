class Shape:
    def area():
        return 0

class Rectangle:
    def __init__ (self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
rectangle = Rectangle(5,6)
print(rectangle.area())