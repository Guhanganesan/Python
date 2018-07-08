a=2
b=0
x=input("Enter a number")
x=int(x)
for a in range(a,x):

    if(x%a==0 and a<=x/2):
        b=1
        break
if(b==0):
    print("Given Number is  prime")
else:
    print("Given number is not prime")

Result:
Enter a number24
Given number is not prime

Result:
Enter a number23
Given Number is  prime
