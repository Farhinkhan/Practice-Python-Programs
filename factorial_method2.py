#Program for factorial using function
def fact(x):
       f=1
       for i in range(1,x+1):
              f=f*i
       return(f)

n=int(input("Enter the number to calculate factorial : "))
factorial=fact(n)
print("Factorial of  {} is : {}".format(n,factorial))


