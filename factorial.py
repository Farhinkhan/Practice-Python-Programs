#P rogram to find Factorail  of a number using iteration
n=int(input("Enter the number to calculate factorial : "))
fact=1
for i in range(1,n+1):
       fact=fact*i

print("Factorial of  {} is : {}".format(n,fact))

