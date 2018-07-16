name="Guhan"
print("guhan" "Ganesan")
print('x\97\x98')
print(name[::-1])#nahuG
x=len(name)
print(x)
for i in range(0,x):
    print(name[i])

i=0
while i<x:
    print(name[i])
    i=i+1

for m in "ABCD":
    print(m)

name="Alagesana"
count=0
for char in name:
     if char=="a":
        count=count+1
print("The number od a is:",count)


Result:

    guhanGanesan
x\97
nahuG
5
G
u
h
a
n
G
u
h
a
n
A
B
C
D
The number od a is: 3
    
    
 data =[20,30,40,45,5.5,6,3,22]
sum=sum(data)
print(sum) # 171.5

slice=data[3:7]
print(slice) # [45, 5.5, 6, 3]

data=["abn","ghjt","df"]
max = max(data)
print(max) # ghjt

length=len(data)
print(length) #3

def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
#print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare) #{16, 1, 4, 9}

numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
numbersSquare = set(result)
print(numbersSquare)  #{16, 1, 4, 9}
print(list(result))


num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))  #[9, 11, 13]

numbers = (1, 2, 3, 4)
numbers=iter(numbers)
print(next(numbers))
print(next(numbers))
print(next(numbers))

Result:
    171.5
[45, 5.5, 6, 3]
ghjt
3
{16, 1, 4, 9}
{16, 1, 4, 9}
[]
[9, 11, 13]
1
2
3











