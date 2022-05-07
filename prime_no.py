# P rogram to check Prime Number
num= int(input("Enter any number: "))
for i in range(2,num):#num=num-1
    if(num%i==0):
     print(num,"is not a prime number")
     break
else:
    print(num,"is a prime number")
