num=153
rem=0
sum=0
#print(num//10)
#print(num % 10)

while num>=1:
    rem = num % 10
    num = num//10
    sum = sum + rem**3

#print (sum)
if sum==153:
    print("Given Number is Armstrong Number")

Result:
     Given Number is Armstrong Number
