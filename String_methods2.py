print("a"+"b")
print("abcd"[2:])
print("abcd"[::-1])
print("abcd"[-1:])
print("\nn")
print(r"\nn")
print("A""B")
print("Periyar Seakkizhar"[4:8])
print(max("Anbu Bala"))
print("Anbu".find("b"))
x="123456"
#654321
print(x.rfind("5"))
print(x[::-1].startswith("6"))
print(chr(ord('c')+1))
print(chr(ord('c')-1))
print("abcd".replace("c","m"))
s="abcd"
print(s.__getitem__(3))
print(len(s))

print("abcd".__contains__("abc")) #true
print("abcd".__contains__("wer")) #False
print("abcd".__contains__("wat")) #False
print("abcd".__contains__("ab"))  #False
print("abcd".__contains__("ab12")) #False

i=10
j=10
print(i.__add__(j)) #i+j
print("abcd".capitalize())
print("abcd".upper())
print("abcd".lower())
print("abcdef".center(7,'1')) #The character ‘1’ is used for padding instead of a space.
print("acabdbhbf".count("b"))
print("mxyyzxyzxzxyy".count('yy', 1)) #Counts the number of times the substring ‘yy’ is present in the given string, starting from position 1
print("xyyzxyzxzxyy".endswith("xyy"))


Result:

ab
cd
dcba
d

n
\nn
AB
yar 
u
2
4
True
d
b
abmd
d
4
True
False
False
True
False
20
Abcd
ABCD
abcd
1abcdef
3
2
True










