t1 = ()
t3 = tuple([1,2,3,4,4]) # tuple from array
t4 = tuple("abc") # tuple from string
t1 = (1, 12, 55, 12, 81)

print(min(t1))
print(max(t1))
print(sum(t1))
print(len(t1))

t = (11,22,33,44,55)
for i in t:
    print(i, end=" ")
print(22 in t)

print(22 not in t)

t=(10,20,"guhan","anbu",35.40,"raja")
print(t[1])
print(t[1:3])
print(t[:3])
print(t[-2:])

m=(1,2,3)
n=(1,3,2)
print(m==n)
s1={1,2,3}
s2={1,3,2}

s1==s2
print(s1==s2)

# print(m.append(5,6,7)) # Error


Result:

1
81
161
5
11 22 33 44 55 True
False
20
(20, 'guhan')
(10, 20, 'guhan')
(35.4, 'raja')
False
True

