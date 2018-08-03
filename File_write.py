f = open("C:\\test\\myfile.txt", "w")
f.write("Hi Guhan How are you")
f.close()

Result:
       Hi Guhan How are you
      
filepath = 'C:\\test\\myfile.txt'
file_open= open(filepath,'r+')
file_open.write("Hi dear guhan\n"
                "How are you\n"
                "Where are you\n")

Result in myfile.txt:
Hi dear guhan
How are you
Where are you
       

       
       
