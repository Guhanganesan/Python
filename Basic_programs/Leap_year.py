num = int(input("Enter any number"))
if num%4==0:
    if num%100==0:
        if num%400==0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
    
Result:-

Enter any number1700
Not leap year

Enter any number1600
Leap year
