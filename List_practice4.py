#-- check first last is 6 ----
def callFirstLast(L):
     #print(L[0])
     #print(L[1])

     if L[0]==6 and L[len(L)-1]==6:
         print("True")
     else:
         print("False")

L=[6,2,3,5,4]
callFirstLast(L)

#-- rotate ---

L=[1,2,3]
M=[]
length=len(L)-1
for i in range(length,-1,-1):
    M.append(L[i])
print(M)


#-- sum of list of elements ---

L=[1,2,3,4,5]
sum=0
for i in range(0,len(L)):
    sum=sum+L[i]

print(sum)

#-- find largest and replace largest with remaining elements

L=[2,3,1,5,4,0]
length=len(L)
temp=0
M=[]
for i in range(0,length):
    for j in range(i+1,length):
           if L[i]>L[j]:
              temp=L[i]
              L[i]=L[j]
              L[j]=temp            

for i in range(0,length):
     M.append(L[length-1])

print(M)

#-------- print middle values only --

L=[[3,5,7],[2,4,7]]
print(len(L[0]))
M=[]
for i in range(0,len(L)):
    for j in range(0,len(L[i])):
         if j==len(L[i])//2:
            M.append(L[i][j])
print(M)






