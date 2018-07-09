a=2
b=0
x=input("Enter a number")
x=int(x)
for a in range(a,x):

    if(x%a==0 and a<=x/2):
        b=1
        print(a)  # divisible
    #else:
         #print(a)

if(b==0):
    print("Given Number is  prime")
else:
    print("Given number is not prime")


  #   x=5
  #   2: 5%2 == 0 false,  2<=5/2 true

  #   3: 5%3 == 0 false  3<=5/2 false

  #   4: 5%4 == 0 false  4<=5/2 false
  #   5: 5%5 == 0 true   5<=5/2 false

  #   x=4
  #   2: 4%2 ==0 true    2<=4/2 true
  #   b=1   better break here

  #  3:  4%3 == 0 false
  #  4:  4%4 == 0 true  4<=4/2 false


Result:

Enter a number8
2
4
Given number is not prime
