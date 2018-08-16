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

    
# List get even and ood values fro list
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


    
    
