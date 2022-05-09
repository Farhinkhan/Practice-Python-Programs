class circle_rectangle:
    def area(self,a=None,b=None):
        if(a!=None and b==None):
         return 3.14*a*a
        elif(a!=None and b!=None):
         return a*b
        else:
            z="No Value Provided"
            return z
    
    
x=int(input("Enter First value : "))
y=int(input("Enter Second Value : "))
cr=circle_rectangle()
.
a1=cr.area(x)
a2=cr.area(x,y)
a3=cr.area()
print("Area of circle is  : ",a1)
print("Area of rectangle is :",a2)
print(a3)
