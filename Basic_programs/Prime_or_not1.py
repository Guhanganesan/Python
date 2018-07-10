x=input("Enter Number")
x=int(x)
if(x>1):
    if(x%2==0):
        print("Number is not prime")
    elif(x%5==0):
        print("Number is not prime")
    elif(x%3==0):
        print("Number is not prime")
    elif(x%7==0):
        print("Number is not prime")
    else:
        print("The number is prime")


Result:
      Enter Number23
      The number is prime
      
Result:
      Enter Number21
      Number is not prime
