filepath = 'C:\\test\\myfile.txt'
file_open= open(filepath,'w')
L=['Hi dear guhan\n', 'How are you\n', 'Where are you\n']
file_open.writelines(L)

#Appends the text
mylist=["Hi","Dear","Friend","How","Are","you"]
for i in range(0,len(mylist)):
     file_open.write(mylist[i]+"\n")
     
Result in myfile.txt:-
Hi dear guhan
How are you
Where are you
Hi
Dear
Friend
How
Are
you
