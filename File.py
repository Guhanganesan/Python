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



