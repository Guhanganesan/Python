t1 = (1,2,3)
t2=(4,5,6)
t=t1+t2
print(len(t))
print(t)
# t[0]=200
# print(t) Error
# del t[0] does not support
print(any(t1))
print(enumerate(t1))
print(list(enumerate(t1)))

for i in enumerate(t1):
    print(i)

for i, j in enumerate(t1):
    print(i, j)

for i, j in enumerate(t1, 5): # index start from 5
    print(i, j)

t1=(2,5,3,1,4)
print(sorted(t1))

t1=(1,2,3,(4,5))
print(t1)
t2=(1,2,3,(5,4))
print(t1==t2) #False, True if 4,5 and 4,5 for both sub set



Result:
    6
    (1, 2, 3, 4, 5, 6)
    True
    <enumerate object at 0x000000CE04C19C60>
    [(0, 1), (1, 2), (2, 3)]
    (0, 1)
    (1, 2)
    (2, 3)
    0 1
    1 2
    2 3
    5 1
    6 2
    7 3
    [1, 2, 3, 4, 5]
    (1, 2, 3, (4, 5))
    False


