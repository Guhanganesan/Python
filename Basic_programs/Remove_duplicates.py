L=[1,1,3,4,2,1,3,5,6,2,1,3]
length=len(L) 
m=length
i=0
while(i<=length):
    for j in range(i+1, m):
        if L[i] == L[j]:
             L.pop(j)
             i=i-1
             #length = length - 1
             m=m-1
             print(L)
             break
    i=i+1
print("After removed duplicates: ")
print(L)

Result:-
[1, 3, 4, 2, 1, 3, 5, 6, 2, 1, 3]
[1, 3, 4, 2, 3, 5, 6, 2, 1, 3]
[1, 3, 4, 2, 3, 5, 6, 2, 3]
[1, 3, 4, 2, 5, 6, 2, 3]
[1, 3, 4, 2, 5, 6, 2]
[1, 3, 4, 2, 5, 6]
After removed duplicates: 
[1, 3, 4, 2, 5, 6]

