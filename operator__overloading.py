#write a python script to add number in test of students

class test:
	def __init__(self,num1,num2):
		self.n1 = num1
		self.n2 = num2 

	def show(self):
		print("--------------------")
		print(self.n1)
		print(self.n2)

	def __add__(self,other):
		x = self.n1 + other.n1
		y = self.n2 + other.n2 
		z = test(x,y)
		return z

try : 

	t1 = test(int(input("Enter Marks of Subject One : ")),int(input("Enter Marks of Subject Two : ")))
	t2 = test(int(input("Enter Marks of Subject One : ")),int(input("Enter Marks of Subject Two : ")))
	t1.show()
	t2.show()

	t3 = t1+t2 

	t3.show()

	t4 = test(12,12)
	t5 = t3 + t4

	#t4.display()
	t5.show()


except ValueError:
	print("Please an Integer Value only")

except AttributeError:
	print("Display is invalid method instead use show")

finally : 
	print("Thanks for Using my Program")
