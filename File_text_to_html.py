import random
import urllib.request

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

html_file = open('C:\\test\\myfile.html','w')
a = my_range
x = -1
scope = vars()
data = ''
for i in a: #TIP: use a generator
     scope['x']+=1
     data += a[x]
     data += '\n'
html_file.write(data)
html_file.close()









