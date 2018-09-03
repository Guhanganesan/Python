set1 = {1, 3,2,5,4,3, 1}
print(set1)

set2={'d','b','a','d','c','a','f'}
print(set2)

set2 = {1, 2, 3, (1, 2, 3), 2.45, "Python", 2, 3}
print(set2)
#(1,2,3) cannot modify the tuple

#List of duplicate elements
theList = [1, 2, 3, 4, 2, 3, 1]
theSet = set(theList)
print(theSet)

#cannot modify the tuple
tuple = (1, 2, 3, 4, 2, 3, 1)
theSet = set(tuple)
print(tuple)
print("#-----------------------------------")

theSet = set()
theSet.add(1)
theSet.add(2)
theSet.add(3)
theSet.add(2)
print(theSet)

#Update
theSet.update([5,7])
print(theSet)

#Remove
theSet.remove(5)
print(theSet)



Result:-
    
{1, 2, 3, 4, 5}
{'c', 'd', 'a', 'b', 'f'}
{1, 2, 3, 2.45, 'Python', (1, 2, 3)}
{1, 2, 3, 4}
(1, 2, 3, 4, 2, 3, 1)
-----------------------------------
{1, 2, 3}
{1, 2, 3, 5, 7}
{1, 2, 3, 7}


