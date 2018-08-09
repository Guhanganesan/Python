num=int(input("Enter any number"))
count=0
while num>=1:
    rem=num%10
    if (rem ==2):
         count+=1
    num=num//10
print(count)

Result:-

Enter any number12325262
4
