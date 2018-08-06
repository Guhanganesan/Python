path="C:\\test\\test.txt"
file_open=open(path,'r')
print(file_open.name)
print(file_open.mode)
print(file_open.closed)

#Read
all_lines = file_open.read()
print(all_lines)

#ReadLine

read_line= file_open.readline()
print(read_line)

Read Lines
read_lines=file_open.readlines()
print(read_lines) # Shows in a list
for line in read_lines:
    print(line.strip())

#-----------------------------------

file_open=open(path,'w')
file_open.write("Hi dear Guhan")

L=[]
for line in range(0,3):
    print("Enter the",line,"st line")
    x=input()
    L.append(x+"\n")
file_open.writelines(L)
file_open.close()

#-----------------------------------

import shutil
shutil.copy2("C:\\test\\test.txt","C:\\test\\Anbu.txt")

#-----------------------------------

with open("C:\\test\\test.txt") as file:
    lines=file.readlines()
    print(lines)#Prints list of lines
for line in lines:
    print(line.strip())
#------------------------------------
