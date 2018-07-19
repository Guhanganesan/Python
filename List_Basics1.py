list = [[2,5,6],[9,6,5]]
print(list[0][1:])

print(list[1][::-1])

list=[1,2,3,5,2,6,2,7,2]
print(list.count(2))

list=[]
for x in range(0,11):
    list.append(x)

print(list)

list= [x for x in range(10) if x>5]
print(list)

list=[ x+y for x in [1,2,3] for y in [4,4,4]]
print(list)

x="Hi dear6 friend"
print(all(x))

max = max(list)
print(max)

min = min(list)
print(min)

length=len(list)
print(length)


Result:

[5, 6]
[5, 6, 9]
4
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[6, 7, 8, 9]
[5, 5, 5, 6, 6, 6, 7, 7, 7]
True
7
5
9
