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
    print("Avg: ", sum/5)
main()

Result:

Enter how many numbers5
Enter Number: 1: 12
Enter Number: 2: 13
Enter Number: 3: 14
Enter Number: 4: 15
Enter Number: 5: 16
Avg:  14.0

