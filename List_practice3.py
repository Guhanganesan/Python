#1:
def f(value, values):
    v = 1
    values[1] = 1
t = 2
v = [2, 1, 3]
f(t, v)
print(t, v[0])

#2:
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element:
                v = element

    return v
print(fun(data[0]))

#3:

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
    #print(arr[i-1])
for i in range(0, 6):
    print(arr[i], end = " ")
    
 Result:
   2 2
4
2
3
4
5
6
2 3 4 5 6 6 
