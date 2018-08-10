data={
    'name':'keerthana',
    'mobile':3878397,
    'age':20
}

print(data)

for key in data:
    print(key)
L=[]
for value in data.values():
    #print(value)
    L.append(value)
print(L)

for value in data.keys():
    print(value)

print(data.get('name'))

data['name']="Pallavi";

print(data)

m = data.pop('name')

print(m)

#print(data)

ex={'stree1':'south'}
data.update(ex)

#print(data)


details={
    'name':'keerthana',
    'mobile':837096,
    'age':20,
    'address':{
        'D/NO':'23',
        'Street':'North'
    }
}

print(details['mobile'])
print(details['address']['Street'])

for key, value in details.items():
    print(key, value)
    
 Result:-
    
{'name': 'keerthana', 'mobile': 9940068591, 'age': 20}
name
mobile
age
['keerthana', 9940068591, 20]
name
mobile
age
keerthana
{'name': 'Pallavi', 'mobile': 9940068591, 'age': 20}
Pallavi
9940068591
North
name keerthana
mobile 9940068591
age 20
address {'D/NO': '23', 'Street': 'North'}
