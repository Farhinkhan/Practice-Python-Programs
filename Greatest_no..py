a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if (a==b==c):
   print("All Numbers are equal")
elif(a==b and a>c):
    print("a,b are equal and c is small")
elif(b==c and b>a):
    print("b,c  are equal and a  is small") 
elif(a>b)and (a>c):
   print(a,"is greater than", b ,"and",c)
elif(b>a) and (b>c):
   print(b," is greater than",a ,"and " ,c)
else:
   print(c, "is greater than",a , "and",b)

   
