#List Searching the element
L=[3,5,2,6,4,1,7,0,8]

length=len(L)-1
m=0
x=int(input("Enter element to search"))
for i in range(0, length):
        if x == L[i]:
            print("The element is available in the position: ",i)
            m=1
if(m==0):
    print("The element is not available")


Result:
      Enter element to search3
      The element is available in the position:  0
Result:
      Enter element to search23
      The element is not available
