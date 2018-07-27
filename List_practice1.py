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


list=[]
sum=0
for i in range(0,3):
    for j in range(0,3):
        list.append((i+j)**2)
print(list)

#Ans:[0, 1, 4, 1, 4, 9, 4, 9, 16]

list=[[2,5,7,8],[2,3,4,5],[4,3,2,1]]
sum=0
for i in range(0,3):
    for j in range(0,3):
        sum=sum+list[i][j]
        
print(sum)

#Ans:32

list=[[2,5,7,8],[2,3,4,5],[4,3,2,1]]
sum=0
for i in range(0,3):
    for j in range(0,3):
        if list[i][j]==2 or list[i][j]==3:
            sum=sum+list[i][j]

print(sum)

#Ans:12


    
    
