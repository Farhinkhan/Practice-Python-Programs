#Program to find square root of a number
#method1
import math
x=int(input("Enter number : "))
y=math.sqrt(x)
print(x)
print(y)

#method2
import math as m
x=int(input("Enter number : "))
y=m.sqrt(x)
print("Square  Root of {} is : {}".format(x,y))


#method3
from math import sqrt 
x=int(input("Enter number : "))
y=sqrt(x)
print("Square Root of",x, "is : ",y)

