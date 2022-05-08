#Program to check if the number is an Armstrong Number or not
num=int(input("Enter a number : "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp//=10
if num==sum:
    print(num,"is an Armstrongm number")
else:
    print(num,"is  not an Armstrongm number")
    
