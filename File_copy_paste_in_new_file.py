import os
filepath = 'C:\\test\\myfile.txt'
file_open= open(filepath,'r+')
file_read=file_open.readlines()
mylist=[]
for i in range(0,len(file_read)):
           mylist.append(file_read[i])

path ='C:\\test\\'

name="Vimal"

if not os.path.exists(path):
    os.makedirs(path)

filename = name +'.txt'
with open(os.path.join(path, filename), 'w') as temp_file:

    for i in range(0,len(mylist)):
        temp_file.write(mylist[i])

Result(myfile.txt):-

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
