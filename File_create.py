filepath = 'C:\\test\\myfile.txt'
file_open= open(filepath,'w')
L=['Hi dear guhan\n', 'How are you\n', 'Where are you\n']
file_open.writelines(L)

#Appends the text
mylist=["Hi","Dear","Friend","How","Are","you"]
for i in range(0,len(mylist)):
     file_open.write(mylist[i]+"\n")

#create new file:

#url='C:\\test\\file1.txt'
#file_create=open(url,'x')


# Create new file and add the contents

import os

path ='C:\\test\\'

name="Suresh" // new file name

mylist=["Hi","Dear","Friend","How","Are","you"]
if not os.path.exists(path):
    os.makedirs(path)

filename = name +'.txt'
with open(os.path.join(path, filename), 'w') as temp_file:

    for i in range(0,len(mylist)):
        temp_file.write(mylist[i]+"\n")
