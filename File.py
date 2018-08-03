import os
filepath = 'C:\\test\\myfile.txt'
file_open= open(filepath,'r+')
#file_read=file_open.read() #reads all text
#print(file_read)

#file_read1=file_open.read(10)
#print(file_read1)

L=[]
for line in file_open:
    L.append(line)
print(L)

s = os.path.getsize("C:\\test\\myfile.txt")
print(s)


print(f.name)


myfile.txt:-
    
Version of PHP?
What is session?
What is cookie?

-------------------------------------------------------

filepath = 'C:\\test\\myfile.txt'
file_open= open(filepath,'r+')
file_open.write("Hi dear guhan\n"
                "How are you\n"
                "Where are you\n")
				
				
Result in myfile.txt:
Hi dear guhan
How are you
Where are you
-------------------------------------------------------

filepath = 'C:\\test\\myfile.txt'
file_open= open(filepath,'r+')
file_read=file_open.readline()
print(file_read)
# Hi dear guhan --> Reads only a single line

------------------------------------------------------

filepath = 'C:\\test\\myfile.txt'
file_open= open(filepath,'r+')
file_read=file_open.readlines()
print(file_read)
#['Hi dear guhan\n', 'How are you\n', 'Where are you\n']
for i in range(0,len(file_read)):
           # print(file_read[i]) # prints data with new line
           print(file_read[i].strip())


Result:
['Hi dear guhan\n', 'How are you\n', 'Where are you\n']
Hi dear guhan
How are you
Where are you
