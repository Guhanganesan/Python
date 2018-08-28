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

Explanation:
    
 i=0, j=1, 3>5 flase
 i=0, j=2, 3>2 true 
      temp =3
      L[0]=2(L[j])
      L[2]=3(temp)
        


Result:

[0, 1, 2, 3, 4, 5, 6, 7, 8]
