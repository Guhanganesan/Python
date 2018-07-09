num=153
rem=0
sum=0
#print(num//10)
#print(num % 10)

while num>=1:
    rem = num % 10
    num = num // 10
    sum = sum + rem

print ("Sum of digits of a number is:",sum)

Result:

Sum of digits of a number is: 9
