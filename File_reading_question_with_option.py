import random
filepath = 'C:\\test\\test.txt'
list=[]
count=1
with open(filepath) as fp:
   line = fp.readline()
   cnt = 0
   while line:
       list.append(line.strip())
       line = fp.readline()
       cnt += 1
#random.shuffle(list)
#my_range=list[0:10]
#for x in range(0,10):
#     print(count,my_range[x])
#     count+=1
#print(random.choice(list))

#data=["I","am","a","python","programmer","hi","Guhan","How","are","u"]
chunks = [list[x:x+3] for x in range(0, len(list),3) if (len(list)%3==0)]
#print(chunks)
random.shuffle(chunks)
random.choice(chunks)
#print(chunks)
#print(random.choice(chunks))

my_range=chunks[0:8]
for x in range(0,8):
     #print(count,my_range[x])
     for j in range(0,len(my_range[x])):
           print(count,my_range[x][j])
           count+=1
 
 
 
 test.txt:-
 
 PHP can support multiple inheritance?
A)      B)
C)      D)
Which function is used to pick one or more random values from array?
A)      B)
C)      D)
Why PHP is truly cross platform?
A)      B)
C)      D)
What is the best way to copy a file in php?
A)      B)
C)      D)
Can PHP embedded in xhtml?
A)      B)
C)      D)
Why we use $_SESSION?
A)      B)
C)      D)
Write the error control operator in PHP.
A)      B)
C)      D)
Write the extension for include the file?
A)      B)
C)      D)
 
