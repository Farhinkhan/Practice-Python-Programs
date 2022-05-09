# program for palindrome number using iterative method
n = int(input("please give a number : "))
reverse,temp = 0,n
while temp!=0:
    reverse = reverse*10 + temp%10;        
    temp=temp//10;
if reverse==n:
    print("Number is palindrom")
else:
    print("Number is not palindrom")
