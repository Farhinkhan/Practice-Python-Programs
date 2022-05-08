class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius
x=int(input("Enter radius to calculate area of a circle : "))
y=int(input("Enter radius to calculate circumference of a circle : "))

a=circle(x)
b=circle(y)
print("area of circle  : ", a.area())
print("circumference of circle : ",b.circumference())
