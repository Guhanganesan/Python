import array 

#a=array.array('a',[3,6,2,7]) #ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
a=array.array('i',[3,5,7,9])
print(a)
print(a[0])
a.append(10)
print(a)
#a.byteswap()
#print(a)

a.extend([1,0,2])
print(a)
print(a.index(0))

a.insert(6,67)
print(a)
a.pop()
print(a)
a.reverse()
print(a)
a.pop(2)
print(a)
a.remove(10)
print(a)
a.__setitem__(1,100)
print(a)
a.__delitem__(2)
print(a)
print(a.__add__(array.array('i',[22,33])) )
print(a)


Result:-

array('i', [3, 5, 7, 9])
3
array('i', [3, 5, 7, 9, 10])
array('i', [3, 5, 7, 9, 10, 1, 0, 2])
6
array('i', [3, 5, 7, 9, 10, 1, 67, 0, 2])
array('i', [3, 5, 7, 9, 10, 1, 67, 0])
array('i', [0, 67, 1, 10, 9, 7, 5, 3])
array('i', [0, 67, 10, 9, 7, 5, 3])
array('i', [0, 67, 9, 7, 5, 3])
array('i', [0, 100, 9, 7, 5, 3])
array('i', [0, 100, 7, 5, 3])
array('i', [0, 100, 7, 5, 3, 22, 33])
array('i', [0, 100, 7, 5, 3])
