#a,b,c,d=10,20,30,40,50
#print(a,b,c,d) --> ValueError

try:
    a=10
    b=0
    user=int(input("Enter a value"))
    print("Open")
    print(a/b)
    print(user)  #
   
except ZeroDivisionError as e:
    print("U cannot divide a number by zero bcz:", e)

except ValueError as e:
    print("Should not use alphabets")

finally:  
    print("Close") 

