#Program to print even numbers
a= int(input("please enter a number:"))
print("Even Numbers from",1,"to",a," : ")
for i in range(1,a+1):
    if(i%2==0):
        print(i,end=' ')
        

