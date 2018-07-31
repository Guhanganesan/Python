#Python Set is an unordered collection of unique elements
set1 = {1, 2, 3, 4, 2, 3, 1}
print(set1)

set2 = {1, 2, 3, (1, 2, 3), 2.45, "Python", 2, 3}
print(set2)

theList = [1, 2, 3, 4, 2, 3, 1]
theSet = set(theList)
print(theSet)

theSet = set()
theSet.add(1)
theSet.add(2)
theSet.add(3)
theSet.add(2)
print(theSet)

#Update
theSet.update([5,7])
print(theSet)

# Remove Element
theSet.discard(3)
print(theSet)

theSet.remove(5)
print(theSet)

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
print(B.issubset(A))

A={1,2,3,4}
B={5,6}
print(A.isdisjoint(B))

m={3,5,4,2,7}
n=m.pop()
print(n)


Result:

{1, 2, 3, 4}
{1, 2, 3, 2.45, 'Python', (1, 2, 3)}
{1, 2, 3, 4}
{1, 2, 3}
{1, 2, 3, 5, 7}
{1, 2, 5, 7}
{1, 2, 7}
{1, 2, 3, 4, 5, 7}
{2, 3}
{1, 4}
{5, 7}
False
True
True
2
