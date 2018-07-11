num=int(input("enter any number"))
sum=0
check=num
while(num>=1):
     rem=num%10
     sum=sum*10+rem
     num = num//10
print(sum)
if(check==sum):
    print("Given Number is Polindrome")
else:
    print("Given Number is not Polindrome")



Result:

enter any number121
121
Given Number is Polindrome
