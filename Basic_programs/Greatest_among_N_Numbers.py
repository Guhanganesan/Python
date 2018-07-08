a=0
x=input("Enter how many numbers to check")
x=int(x);
for x in range(a,x):
    print("Enter Number",(x+1))
    number = input()
    number=int(number)
    if(number>a):
        a=number
print("The Largest Number is", a)

Result:

Enter how many numbers to check4
Enter Number 1
4
Enter Number 2
2
Enter Number 3
8
Enter Number 4
3
The Largest Number is 8
