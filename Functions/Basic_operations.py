#Basic Operations
	def add(x,y):
		return x+y
	def mul(x,y):
		return x*y
	def sub(x,y):
		return  x-y
	def main():
		a=add(20,10)
		b=mul(20,10)
		c=sub(20,10)
		print(a,b,c)
	main()

Result:
    30 200 10
	
	def add(x,y):
		return x+y
	def mul(x,y):
		return x*y
	def sub(x,y):
		return  x-y
	a,b,c=0,0,0
	def main():
		global a,b,c
		a=add(20,10)
		b=mul(20,10)
		c=sub(20,10)
	main()
	print(a,b,c)

Result:

30 200 10


