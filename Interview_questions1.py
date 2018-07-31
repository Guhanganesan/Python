#1:
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(3,[3,2,1])

#2:
roots={ (x**2)**0.5 : x for x in range(5,0,-1) if x<4}
print(roots)

#3:
for i in range(7):
    if i==3:
        break
    print(i)

#4:
for i in range(7):
    if i == 3:
        continue
    print(i)

#5:
def A(x):
    def B():
        print(x)
    return B
A(8)()

#6:
c,p,s,i,m =1,7,1,0,0
while (c):
	s+=s*p%2
	p-=1
	if p ==0 :
	 break
	i+=1
	m=m+s
print(m/i)

#7:
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
     for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

#8:
num = 12
for i in range(1, 11):
   print(num,'x',i,'=',num*i)

Result:-

[3, 2, 1, 0, 1, 4]
{3.0: 3, 2.0: 2, 1.0: 1}
0
1
2
0
1
2
4
5
6
8
2.0
[17, 15, 4]
[10, 12, 9]
[11, 13, 18]
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120
