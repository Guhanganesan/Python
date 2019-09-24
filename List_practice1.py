
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

    
# List get even and odd values fro list
L=["Tamil","English","Maths","Science","Social"]
length=len(L)
Even=[]
Odd=[]
for i in range(0,length):
    if  i%2==0:
        Even.append(L[i])
    if  i%2!=0:
        Odd.append(L[i])
print("Even Elements:")
print(Even)
print("Odd Elements:")
print(Odd)

Result:
    
Even Elements:
['Tamil', 'Maths', 'Social']
Odd Elements:
['English', 'Science']

#-----------------------------------------------------------

#Find index of list
L=["Tamil","English","Maths","Science"]
length=len(L)
search=input("Enter which element to get the index value")
for i in range(0,length):
     if search==L[i]:
         print("The element",L[i]," is located at ",i,"th position")
         break
 #Result
Enter which element to get the index valueEnglish
The element English  is located at  1 th position

#------------------------------------------------------------

#Replace the element at specified location
L=["Tamil","English","Maths","Science"]
length=len(L)
index=int(input("Enter the index value"))
result="The Elements are:"
replace=input("Enter the element to replace")
for i in range(0,length):
     if replace!=L[index]:
         L[index]=replace
         break
     if replace == L[index]:
         result="The same element is found, Try to add another"
         continue
print(result)
print(L)

Result:-
Enter the index value2
Enter the element to replaceMaths
The same element is found, Try to add another
['Tamil', 'English', 'Maths', 'Science']

Result:-
    
Enter the index value2
Enter the element to replacePhysics
The Elements are:
['Tamil', 'English', 'Physics', 'Science']

#-----------------------------------------------------------------
  
#Remove the element
L=["Tamil","English","Maths","Science"]
length=len(L)
result="The Elements are:"
remove=input("Enter the element to remove")
for i in range(0,length):
     if remove==L[i]:
         L.pop(i)
         break
     if remove!= L[i]:
         continue
print(result)
print(L)

Result:-
Enter the element to removeEnglish
The Elements are:
['Tamil', 'Maths', 'Science']

Result:-
Enter the element to removeBiology
The Elements are:
['Tamil', 'English', 'Maths', 'Science']
#----------------------------------------------------------------
#Get list of values from given range
L=["Tamil","English","Maths","Science","Social","Biology"]
start=int(input("Enter starting index"))
end=int(input("Enter ending index"))
length=len(L)
new_list=[]
for i in range(0,length):
    if(i>=start and i<=end):
        new_list.append(L[i])
        start+1
print(new_list)

Result:-
Enter starting index2
Enter ending index4
['Maths', 'Science', 'Social']

#----------------------------------------------------------------
#Insert list of elements in a given range
L=["Tamil","English","Maths","Science","Social","Biology"]
start=int(input("Enter starting index"))
end=int(input("Enter ending index"))
length=len(L)
new_list=[]

test=start
while(start<=end):
    print("Enter element for index", start)
    get = input()
    new_list.append(get)
    start+=1
j=0
for i in range(0,length):
    if(i>=test and i<=end):
        L[i]=new_list[j]
        test=test+1
        j=j+1
print(L)

Result:-
Enter starting index2
Enter ending index4
Enter element for index 2
Ethics
Enter element for index 3
Zoology
Enter element for index 4
Politics
['Tamil', 'English', 'Ethics', 'Zoology', 'Politics', 'Biology']
#--------------------------------------------------------------------
# Remove range of elements in a list

L=["Tamil","English","Maths","Science","Social","Biology"]
no_of=int(input("Enter how many elements you want to remove"))
start=int(input("Enter starting index"))
length=len(L)
count=1
for i in range(0,length):
    if( start<=i and count<=no_of):
        L.pop(start)
        length=length-1
        count=count+1
print(L)

Result:-
Enter how many elements you want to remove3
Enter starting index1
['Tamil', 'Social', 'Biology']

#-------------------------------------------------------------
#To find second largest in a list
L=[2,5,1,3,6,8,7,9,4]
length=len(L)
greatest=0
new_list=[]
for i in range(0,length):
    if greatest<L[i]:
       greatest=L[i]
       new_list.append(greatest)
print(greatest)
print(new_list)
new_length=len(new_list)
print(new_list[new_length-2])

Result:-
9
[2, 5, 6, 8, 9]
8
#-----------------------------------------------------------

#Remove Duplicates in a list

L=[4,3,2,3,4,2,5,6,5,7,2,1,4,9,6]
length=len(L) 
i=0
while(i<=length):
    for j in range(i+1, length):
        if L[i] == L[j]:
             L.pop(j)
             i=i-1
             length = length - 1
             print(L)
             break
    i=i+1
print("Origial List: ")
print(L)

Result:
    
[4, 3, 2, 3, 2, 5, 6, 5]
[4, 3, 2, 2, 5, 6, 5]
[4, 3, 2, 5, 6, 5]
[4, 3, 2, 5, 6]
After removed duplicates: 
[4, 3, 2, 5, 6]

#-----------------------------------------------------------
#Remove Element

L=[23,45,56,78,43]
check=False
element=int(input("Enter Element to Remove"))
for i in range(0,len(L)):#0,5
    if element==L[i]:
        L.remove(element)
        check=True
        break
if(check==False):
    print("Not Found")      

print(L)

#------------------------------------------------------------
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

#------------------------------------------------
#Sorting
L=[2,3,1,5,0,6,-2,4]
length=len(L)
temp=0
for i in range(0,length):
    for j in range(i+1,length):
           if L[i]>L[j]:
              temp=L[i]
              L[i]=L[j]
              L[j]=temp            

print(L)
#--------------------------------------------------
#Second Largest
L=[2,3,1,5,0,6,-2,4]
length=len(L)
first=0
second=0
for i in range(0,length):
           if L[i]>first:
               second=first
               first=L[i]
           elif L[i]>second:
               second=L[i]

print(first)
print(second)


#-----------------------------------------------------

#Second Minimum
L=[2,3,1,5,0,6,-2,4]
length=len(L)
first=L[0]
second=L[0]
for i in range(0,length):
           if L[i]<first:
               second=first
               first=L[i]
           elif L[i]<second:
               second=L[i]

print(first)
print(second)

#--------------------------------------------------------
