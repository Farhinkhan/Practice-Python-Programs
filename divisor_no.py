'''create a program that asks the user for a number and then prints
outs a list of all the divisors of that number.'''

n=int(input("Enter the number to find its divisor : "))
print("The divisor of",n,"is :")
for i in range(1,n+1):
    if(n%i==0):
        print(i ,end=' ')
