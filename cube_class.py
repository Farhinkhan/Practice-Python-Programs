class cube:
    def __init__(self,side):
        self.side=side
    def area(self):
        return 6*self.side*self.side
    def volume(self):
        return self.side*self.side*self.side
x=int(input("Enter  the side of a cube : "))
a=cube(x)
print("Area of cube : ",a.area())
print("volume of cube : ",a.volume())
