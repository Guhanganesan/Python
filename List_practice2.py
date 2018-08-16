# Interchange a given string
name="Raghava Guhan"
name = name.split();
print(name)
name.reverse()
print(name)
name=" ".join(name)
print(name)


Result:

  ['Raghava', 'Guhan']
  ['Guhan', 'Raghava']
  Guhan Raghava

list=[]
sum=0
for i in range(0,3):
    for j in range(0,3):
        list.append((i+j)**2)
print(list)

#Ans:[0, 1, 4, 1, 4, 9, 4, 9, 16]

list=[[2,5,7,8],[2,3,4,5],[4,3,2,1]]
sum=0
for i in range(0,3):
    for j in range(0,3):
        sum=sum+list[i][j]
        
print(sum)

#Ans:32

list=[[2,5,7,8],[2,3,4,5],[4,3,2,1]]
sum=0
for i in range(0,3):
    for j in range(0,3):
        if list[i][j]==2 or list[i][j]==3:
            sum=sum+list[i][j]

print(sum)

#Ans:12
