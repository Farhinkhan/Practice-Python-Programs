#Fibonacci Series
n=int(input("Enter any number : "))
n1=0
n2=1
print("Fibonacci Series :")
if(n>0):
    print(n1,end=' ')
    print(n2,end=' ')
    for i in range(2,n+1):
        n3=n1+n2
        print(n3 ,end=' ')
        n1=n2
        n2=n3
else:
    print("Invalid Input")
