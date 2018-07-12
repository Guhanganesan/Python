name="Guhan"
list_of_details=list(name)
print(list_of_details)
#Escape Sequence
print('"Hi"')
print('\"Hi\"')
print('he is my sisters\'s friend')
print('\no')
print("\\no")
#Raw String to ignore escape sequence
print(r"\no")

#Format method
# {} -> Replacement fields

x="{},{},{}".format("Guhan","Anbu","Ragav")
print(x)
m="{}".format("Guhan","Anbu","Ragav")
print(m)

n="{},{}".format("Guhan","Anbu","Ragav")
print(n)



Result:

['G', 'u', 'h', 'a', 'n']
"Hi"
"Hi"
he is my sisters's friend

o
\no
\no
Guhan,Anbu,Ragav
Guhan
Guhan,Anbu
