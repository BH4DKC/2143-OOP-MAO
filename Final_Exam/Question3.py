class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[%d,%d]" % (self.x, self.y)

class Shape(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        pass


class Square(Shape):
    def __init__(self, width):
        Shape.__init__(self, width, width) #Call the init function of Shape
    def area(self): #Returns the area of a square based on the given data
        return self.p1 * self.p1
    def perimeter(self): # Returns the perimeter of a square based on the given data
        return 4*self.p1

class Rectangle(Shape):
    def __init__(self,width, height):
        Shape.__init__(self,width, height)
    def area(self):
        return self.p1*self.p2
    def perimeter(self):
        return 2*(self.p1+self.p2)

class Cube(Square):
    def __init__(self,sl):
        Square.__init__(self,sl,)
        self.height=sl
    def surfaceArea(self): # returns the volume of the cube
        return self.height * Square.area(self)
    def perimeter(self):
        return 3 * Square.perimeter(self)
