#Program to print Table of Number
n= int(input("Enter a value:"))
m=n*10
count=1
for i in range(n,m+1,n):
   print("{}*{}={}".format(n,count,i))
   count=count+1
    
