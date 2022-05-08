
def Add(x,y):
    z=x+y
    return z
def Sub(x,y):
    z=x-y
    return z
def Mul(x,y):
    z=x*y
    return z
def Div(x,y):
    z=x/y
    return z
def Mod(x,y):
    z=x%y
    return z
def for_power(x,y):
    return (x**y)
def Square(x):
    z=x*x
    return z
def Cube(x):
    z=x*x*x
    return z
def square_root(x):
    z=x**0.5
    return z
def cube_root(x):
    z=(x*x*x)/3
    return z

    
    



print("Welcome to Farheen's Calculator")

choice= input("Enter the value(int or float ) which u want: ")
if(choice=='int'):
    a=int(input("Enter first value : "))
    b=int(input("Enter second value : "))
elif(choice=='float'):
    a=float(input("Enter first value : "))
    b=float(input("Enter second value : "))
else:
    print("Please choose integer value or float value.")

print("1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Modulo")
print("6.Power\n 7.square\n 8.cube")
print("9.Square_Root\n 10.Cube_Root")
opr= int(input("Enter value to perform Operation : "))
if(opr== 1):               
    x=Add(a,b)
    print("Addition of " ,a,"+",b,"=",x)
elif(opr== 2):
    x=Sub(a,b)
    print("Subtraction of " ,a,"-",b,"=",x)
elif(opr==3):
    x=Mul(a,b)
    print("Multiplication of ",a,"*",b,"=",x)  
elif(opr==4):
    if(b!=0):
       x=Div(a,b)
       print("Division of ",a,"/",b,"=",x)
    else:
        print("Zero division error")
elif(opr==5):
    x=Mod(a,b)
    print("MOdulo of ",a,"%",b,"=",x)
elif(opr==6):
    x=for_power(a,b)
    print("power of ",a,"**",b,"=",x)
    
elif(opr==7):
    x=Square(a)
    print("Square of ",a,"is" ,x)
elif(opr==8):
    x=Cube(a)
    print(" Cube of ",a,"is" ,x)
    
elif(opr==9):
    x=square_root(a)
    print("Square  root of ",a,"is" ,x)
elif(opr==10):
    x=cube_root(a)
    print("cube root  of ",a,"is" ,x)
    
else:
    print("Invalid Choice.")

    

      


    
    
