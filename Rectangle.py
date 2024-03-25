class Rectangle:
    """Rectangle"""
    def __init__(self, height, width):
        """Self"""
        self.height = height
        self.width = width
    def area(self):
        """Calculate Area"""
        return self.height * self.width

    def perimeter(self):
        """Calucalate perimeter"""
        return 2 * (self.height + self.width)
height = float(input())
width = float(input())
condition = input()
rectangle = Rectangle(height, width)
if condition == "area":
    result = rectangle.area()
else:
    result = rectangle.perimeter()
print("%.2f" % result)
