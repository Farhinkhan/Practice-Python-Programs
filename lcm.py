#Program to find LCM of two numbers
def cal_lcm(x,y):
    if(x>y):
        max=x
    else:
        max=y
    while(True):
        if(max%x==0 and max%y==0):
            lcm=max
            break
        max+=1
    return lcm


x=int(input("Enter First Value : "))
y=int(input("Enter Second Value : "))
lcm=cal_lcm(x,y)
print("The LCM is : ",lcm)
