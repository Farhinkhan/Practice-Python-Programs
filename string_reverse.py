#method1:program for string reversal using for loop
str1=input("Enter a string:")
x=len(str1)
str2=" "
for i in range(x-1,-1,-1) :
    str2+=str1[i]
print(str2)


#method2:string reversal using slicing
print(str1[::-1])
    


