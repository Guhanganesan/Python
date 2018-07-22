#List average
def main():
      list=[]
      sum=0.0
      x=int(input("Enter how many numbers"))
      for i in range(1,x+1):
           num = eval( input("Enter Number: "+ str(i)+ ": "))
           list = list+[num]
      length=len(list)
      for j in range(0,length):
           sum=sum+list[j]
      print("Avg: ", sum/x)
main()

Result:-

    Enter how many numbers4
    Enter Number: 1: 12
    Enter Number: 2: 13
    Enter Number: 3: 14
    Enter Number: 4: 15
    Avg:  13.5

#Mini Calculator
def main():
    x=input("enter choice(+/-/*/%): ")
    a=int(input("enter first number"))
    b=int(input("Enter second number"))
    if x=="+":
        print(a+b)
    elif x=="-":
        print(a-b)
    elif x=="*":
        print(a*b)
    elif x=="%":
        print(a/b)
main()

Result:
      enter choice(+/-/*/%): %
      enter first number12
      Enter second number4
      3.0
      
#Mini Calculator using functions

def add(a,b):
    return  a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def main():
    x=input("enter choice(+/-/*/%): ")
    a=int(input("enter first number"))
    b=int(input("Enter second number"))
    if x=="+":
        print(add(a,b))
    elif x=="-":
        print(sub(a,b))
    elif x=="*":
        print(mul(a,b))
    elif x=="%":
        print(div(a,b))
main()

Result:
      enter choice(+/-/*/%): +
      enter first number12
      Enter second number12
      24
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
