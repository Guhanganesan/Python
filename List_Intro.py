#List is a collection which is ordered and changeable. Allows duplicate members.
#list() constructor to make a list


list=["Tamil","English","Maths"]
print(len(list))
list.pop()
print(list)
list.append("Maths")
print(list)
list.pop(1)
print(list)
list.insert(1,"English")
print(list)
del(list[0])
print(list)
list.extend(["Science","Social","Physics"])
print(list)
del(list[2])
print(list)
list.remove("Maths")
print(list)
list.reverse()
print(list)
print(list.count("Social"))
copy=list.copy()
print(copy)
clear=copy.clear()
print(clear)
list.sort()
print(list)
print(list.__contains__("Physics"))
list.__delitem__(0)
print(list)
item=list.__getitem__(0)
print(item)

Result:-
    
	3
['Tamil', 'English']
['Tamil', 'English', 'Maths']
['Tamil', 'Maths']
['Tamil', 'English', 'Maths']
['English', 'Maths']
['English', 'Maths', 'Science', 'Social', 'Physics']
['English', 'Maths', 'Social', 'Physics']
['English', 'Social', 'Physics']
['Physics', 'Social', 'English']
1
['Physics', 'Social', 'English']
None
['English', 'Physics', 'Social']
True
['Physics', 'Social']
Physics







