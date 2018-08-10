details={
    'name':'guhan',
    'age':28,
    'mob':98698,
    'dob':'05/06/90'
}

for key in details:
    print(key)
for value in details.values():
    print(value)

mob ={
    'n1':98689,
    'n2':87588,
    'n3':54356
}

sort = sorted(mob.values())
for value in range(0, len(sort)):
    print(sort[value])
    
    
Result:-

name
age
mob
dob
guhan
28
98698
05/06/90
54356
87588
98689
