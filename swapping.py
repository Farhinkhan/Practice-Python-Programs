#program to swap two numbers
#method1
print("This program is involved to swap the values of two data variables using a third temporary variable")
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
'''print("Values Before Swapping : ")
print("a=",a)
print("b=",b)'''


#method2
'''temp=a
a=b
b=temp'''
''''
a=a+b
b=a-b
a=a-b'''

#method3
a,b=b,a
print("Values After Swapping : ")
print("a=",a)
print("b=",b)
