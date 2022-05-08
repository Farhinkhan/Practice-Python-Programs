#Program to concatenate two list
#using'+'operator

list1=["Smith","Jhon","Ram","Joy"]
list2=[1,2,3,4]
list3=list1+list2
print("Concatenates list using + :",list3)

#using extend()
list1=["Smith","Jhon","Ram","Joy"]
list2=[1,2,3,4]
list1.extend(list2)
print("Concatenates list using extend() :",list3)
