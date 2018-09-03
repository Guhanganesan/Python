#Python set operations

A={1,2,3,4}
B={2,3,5,7}
    #Union-all unique elements of two sets.
print(A.union(B))
    #Intersetion - common unique elements of two sets.
print(A.intersection(B))
    # Difference -set containing items from set A which are not common in set B
print(A.difference(B))
print(B.difference(A))

A={1,2,3,4}
B={2,4}

print(A.issubset(B))
print(A.issuperset(B))
print(B.issubset(A))

A={1,2,3,4}
B={5,6}
print(A.isdisjoint(B))

#Remove the lowest element
m={3,5,4,1,7,2}
n=m.pop()
print(n)
print(m)
n=m.pop()
print(n)
print(m)
#--cannot pop(index or element)
n=m.pop(4)
print(n)
print(m)

#---------------------------------------------------

Result:-
{1, 2, 3, 4, 5, 7}
{2, 3}
{1, 4}
{5, 7}
False
True
True
True
1
{2, 3, 4, 5, 7}
2
{3, 4, 5, 7}



