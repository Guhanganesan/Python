s="Guhan"
print(set(s))

set=set(s)
L=list(set)
print(L)


A={1,2,3}
#print(A[0]) Error
A.add(4)
print(A)

A.add((5,6))
print(A)

A.update([7,8])
print(A)

A.update({9,10})
print(A)

Result:

{'h', 'n', 'a', 'G', 'u'}
['h', 'n', 'a', 'G', 'u']

{1, 2, 3, 4}
{1, 2, 3, 4, (5, 6)}
{1, 2, 3, 4, 7, (5, 6), 8}
{1, 2, 3, 4, 7, (5, 6), 8, 9, 10}


