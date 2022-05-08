#Program to print Permutation(nPr) of a no.
#method1:using function
'''def fact(x):
    fact_x=1
    for i in range(1,x+1):
        fact_x*=i
    return(fact_x)
    
n=int(input("Enter the total items : "))
r=int(input("Enter the no. of items to be arrange : "))
fx=fact(n)
fy=fact(n-r)
p=fx/fy
print("Permutation is :",p)'''




#method2
import factorial as f
x=int(input("enter total items : "))
y=int(input("Enter the no. of items to be arrange : "))
fx=f.fact(x)
fy=f.fact(x-y)
p=fx/fy
print("permutation is :",p)




#method3:without function
'''
#calculate n factorial
fact_n=1
for i in range(1,n+1):
    fact_n*=i 
#calculate n-r factorial
x=n-r
fact_x=1
for i in range(1,x+1):
    fact_x*=i
    
p=fact_n/fact_x
print("Permutation is :",p)'''




