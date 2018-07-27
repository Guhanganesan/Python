# Check subset of list
list1 = [2,4,6,3,5,8,7]
list2=[3,5,2]
l2=len(list2)
l1=len(list1)
count=0
for i in range(0, l2):
    for j in range(0, l1):
           if list2[i]==list1[j]:
               count=count+1
if l2==count:
    print("It is sub set of list")
else:
    print("It is not subset of list")

Result:
    It is sub set of list
    
 
