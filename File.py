import os
f = open("C:\\test\\myfile.txt", "r+")
#str = f.read(10); # only for 10 characters
#print(str);

L=[]
for line in f:
      # print(line)
      L.append(line)
print(L)

s = os.path.getsize("C:\\test\\myfile.txt")
print(s)


print(f.name)



