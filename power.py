#program to calculate power using for loop
base = int(input("Enter the value for base :"))
exponent = int(input("Enter the value for exponent :"))
result=1;
print(base,"to power ",exponent,"=",end = ' ')
for exponent in range(exponent, 0, -1):
    result *= base
print(result)
