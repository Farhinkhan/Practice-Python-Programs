#Program to print pattern
n=int(input("Enter  the  number of row : "))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end='')
    for k in range(0,2*i+1):
        print("*",end='')
    print()
