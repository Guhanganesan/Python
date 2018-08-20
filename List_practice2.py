# Interchange a given string
name="Raghava Guhan"
name = name.split();
print(name)
name.reverse()
print(name)
name=" ".join(name)
print(name)


Result:

  ['Raghava', 'Guhan']
  ['Guhan', 'Raghava']
  Guhan Raghava
#-----------------------------------------------------------
#Total of 1 student marks
L=[]
i = int(input("Enter how many marks"))
sum=0.0
for k in range(0,i):
    print("Enter mark: ",k+1)
    x=int(input())
    L.append(x)
for j in range(0, len(L)):
    sum=sum+L[j]
print(sum)

Result:-
Enter how many marks5
Enter mark:  1
13
Enter mark:  2
12
Enter mark:  3
13
Enter mark:  4
12
Enter mark:  5
13
63.0

#------------------------------------------------------------------
#Total of 3 student marks
L=[[],[],[]]
m = int(input("Enter how many students"))
sum=0.0
for i in range(0,m):
    for j in range(0,m):
     print("Enter student:",i+1,"mark :",j+1)
     x=int(input())
     L[i].append(x)

print(L)

#Sum of total of students marks
sum=0.0
total=[[],[],[]]
for i in range(0,m):
    for j in range(0,m):
        sum=sum+L[i][j]
    total[i].append(sum)
print("Total of individual marks:",total)

#To find greatest values
greatest=0.0
length=len(total)-1
count=0
greatest=0.0
while(length>=0):
    if greatest<int(total[count][0]):
        greatest=total[count][0]
    count=count+1
    length-=1

print("Student has highest mark is:", greatest)

Result:-
Enter how many students3
Enter student: 1 mark : 1
12
Enter student: 1 mark : 2
13
Enter student: 1 mark : 3
14
Enter student: 2 mark : 1
15
Enter student: 2 mark : 2
16
Enter student: 2 mark : 3
17
Enter student: 3 mark : 1
18
Enter student: 3 mark : 2
19
Enter student: 3 mark : 3
20
[[12, 13, 14], [15, 16, 17], [18, 19, 20]]
Total of individual marks: [[39.0], [87.0], [144.0]]
Student has highest mark is: 144.0
  
#-------------------------------------------------------------
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
