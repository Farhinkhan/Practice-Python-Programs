print("This program is to find Area of a circle.")
radius=float(input("Enter the radius of circle : "))
area=3.14*radius*radius
print("Area of Circle is:",area)

#using function
def circle_area(r):
    a=3.14*r*r
    return a

radius=float(input("Enter the radius of circle : "))
area=circle_area(radius)
area=round(area,3)
print("Area of Circle is:",area)

