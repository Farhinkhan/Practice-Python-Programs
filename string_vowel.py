#Program to remove vowels from the string
string = input("Enter a String : ") 
result=''
for i in string:  
    if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):  
        i = ''  
    result += i 
print("String after removing the vowels :",result)
