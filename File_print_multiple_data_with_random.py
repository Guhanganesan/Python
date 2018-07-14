import random
filepath = 'C:\\test\\myfile.txt'
list=[]
count=1
with open(filepath) as fp:
   line = fp.readline()
   cnt = 0
   while line:
       list.append(line.strip())
       line = fp.readline()
       cnt += 1
random.shuffle(list)
my_range=list[0:10]
for x in range(0,10):
     print(count,my_range[x])
     count+=1
#print(random.choice(list))

Result:

1 rt
2 Tera
3 mk
4 Ntrew
5 ws
6 Anbu
7 yu
8 ji
9 sf
10 Kiol
