#List Sorting Ascending Order 
L=[3,5,2,6,4,1,7,0,8]
length=len(L)-1
temp=0

for i in range(0, length):
    for j in range(i+1, length):
        if L[i] > L[j]:
             temp=L[i]
             L[i]=L[j]
             L[j]=temp

print(L)

Result:

[0, 1, 2, 3, 4, 5, 6, 7, 8]

