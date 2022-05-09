#method Overloading when a class have multiple method with same name but with different no. parameter
#method1

"""def _init_(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c"""
"""
		average = 0
		if (a!=None and b !=None and c!=None):
			average = (a+b+c)/3
		elif(a!=None and b!=None and c==None):
			average = (a+b)/2
		elif(a!=None and b==None and c==None) :
			average = a 
		else : 
			average = "No values provided"

		return average

#method2	"""
class student:

	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c

		average = 0
		if (a!=None and b !=None and c!=None):
			average = (a+b+c)/3
		elif(a!=None and b!=None and c==None):
			average = (a+b)/2
		elif(a!=None and b==None and c==None) :
			average = a 
		else : 
			average = "No values provided"

		return average
	
#method3
'''def avg(self, *x):
		average = 0
		sum = 0
		if len(x) == 0 :
			average = "No Values Provided"
		else:
			for i in x :
				sum +=i

			average = sum/len(x)

		return average'''



s1 = student()
#avg5 = s1.avg(12,112,154,12,452,4,35,2,1,5,5,32,1,3,6,3,1,3,4,5,3,2,3,1)
avg1 = s1.avg(12,13,14)
avg2 = s1.avg(12,13)
avg3 = s1.avg(12)
avg4 = s1.avg()


#print(avg1)
#print(avg5)
print(avg1)
print(avg2)
print(avg3)
print(avg4)
