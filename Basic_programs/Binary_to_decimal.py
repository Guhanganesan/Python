num=1110
count =0
sum=0
while(num>=1):
    rem=num%10
    sum= sum+rem*(2**count)
    num = num // 10
    count=count+1

print(sum)


Result:

14

