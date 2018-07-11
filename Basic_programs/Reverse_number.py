num=int(input("enter any number"))
sum=0
while(num>=1):
     rem=num%10
     sum=sum*10+rem
     num=num//10

print(sum)

Result:
enter any number1234
4321
