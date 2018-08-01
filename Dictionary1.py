d ={'name':'anbu','age':25,'mob':866}
print(d.get('name'))
print(d.pop('mob'))
print(d)
del d['age']
print(d)

d1={'mob':67587}
d.update(d1)
print(d)
d['name']="Tera" # update existing value
print(d)



Result:

anbu
866
{'name': 'anbu', 'age': 25}
{'name': 'anbu'}
{'name': 'anbu', 'mob': 67587}
{'name': 'Tera', 'mob': 67587}


