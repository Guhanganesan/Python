#List is a collection which is ordered and changeable. Allows duplicate members.
#list() constructor to make a list

books= list(("Tamil","English","Maths"))
print(books)

books=['Tamil', 'English', 'Maths']
books.append("Science")
print(books)

books.reverse()
print(books)

print(books.count("Tamil"))

x=books.copy()
print(x)

m=x.clear()
print(m)

m=books.pop()
print(m)

print(books)

m=books.pop(1)
print(m)

print(books)

books.insert(1,"Chemaistry")
print(books)

books.extend(["History","Physics"])
print(books)

books.sort()

print(books)


print(books.__contains__("Physics"))

Result:-

['Tamil', 'English', 'Maths']
['Tamil', 'English', 'Maths', 'Science']
['Science', 'Maths', 'English', 'Tamil']
1
['Science', 'Maths', 'English', 'Tamil']
None
Tamil
['Science', 'Maths', 'English']
Maths
['Science', 'English']
['Science', 'Chemaistry', 'English']
['Science', 'Chemaistry', 'English', 'History', 'Physics']
['Chemaistry', 'English', 'History', 'Physics', 'Science']
True





