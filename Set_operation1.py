A={1,2,3,5,7,9}
B={2,4,3,6}
C={2,3}
print(A & B)
print(A | B)
print( A ^ B)
print(A <= B)
print(C<=A)
print(A>=C)
print(A.issuperset(B))
print(A.issuperset(C))


Result:-


{2, 3}
{1, 2, 3, 4, 5, 6, 7, 9}
{1, 4, 5, 6, 7, 9}
False
True
True
False
True

