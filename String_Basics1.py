#1. Reverse a String

	x="Guhan"
	print(x[0])
	len=len(x)
	print(len)
	len=len-1
	name=''
	while len>=0:
		name=name+x[len]
		len=len-1
		print(name)
Result:
		G
		5
		n
		na
		nah
		nahu
		nahuG	

#2. Fequency of occurance of String

	x = str(input("Enter a String "))
	y = str(input("enter a char to check the frequencys "))
	freq = ''
	length = len(x) - 1
	while length >= 0:
		if x[length] == y[0]:
			freq = freq + x[length]
		length = length - 1
	print(freq)
	print("The freq of occurance of String is: ",len(freq))

	Result:

			Enter a String arivukkannan
			enter a char to check the frequencys n
			nnn
			The freq of occurance of String is:  3




#3. Check Palindrome of a String

		x = str(input("Enter a String "))
		# aba == aba --> 2==0 --> 1==1 0==0
		# length-1 ==>  4 ==0 3==1 2==2 1==3 0==4
		length = len(x) - 1
		count=0
		freq=''
		while length >= 0:
			if x[length] == x[length-length+count]:
				freq = freq + x[length]
			count=count+1
			length = length - 1
		if x==freq:
			print("Given string",freq,"is a palindrome")
		else:
			print("Given string is not a palindrome")
	
			
#.4 Max occuring character in String
	x ="Kannan"
	length=len(x)
	count=0
	freq=''
	max=1
	list=[]
	for i in range(0,length):

			for j in range(0, length):
					if x[i]==x[j]:
					 freq=freq+x[i]
			list.append(freq)
			freq=''

	print(list)
	list = set(list) # remove duplicates and gives random values
	print(list)
	print(max(list))
	
# 5. Remove duplicates in string
x=''
name="abacdcda"
list=[]
length=len(name)
for i in range(0,length):
    for j in range(0,length):
     if name[i]==name[j]:
         x=x+name[i]
         list.append(x)
     x=''
print(list)
list=set(list)
list=''.join(list)
print(list)

Result:
	['a', 'a', 'a', 'b', 'a', 'a', 'a', 'c', 'c', 'd', 'd', 'c', 'c', 'd', 'd', 'a', 'a', 'a']
bcda



	

