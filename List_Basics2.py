#Create a list
L =list()
print(L)
L=[]
print(L)
L=list([1,2,3])
print(L)

#Using While loop

list = [3,5,2,4,1,7,6]
length= len(list)-1
i=0
while i<=length:
    print(list[i])
    i=i+1

print(sum([3,5,2,4,1,7,6]))

print(list[::-2])

print(list[::-3])

print(list[::2])

print(list[::3])

list=["Anbu","Kamal","Raja","Kesavan"]
print(list[-2][-2])

print(list[:])

list=[1,2]
print(list *2)

print("Hi Guhan how are you".split())

print("G@u@h@a@n".split('@'))


Result:

[]
[]
[1, 2, 3]
3
5
2
4
1
7
6
28
[6, 1, 2, 3]
[6, 4, 3]
[3, 2, 1, 6]
[3, 4, 6]
j
['Anbu', 'Kamal', 'Raja', 'Kesavan']
[1, 2, 1, 2]
['Hi', 'Guhan', 'how', 'are', 'you']
['G', 'u', 'h', 'a', 'n']














