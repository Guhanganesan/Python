Python dictionary is an unordered collection of items. 
While other compound data types have only value as an element, a dictionary has a key: value pair.
Dictionaries are optimized to retrieve values when the key is known.

A dictionary is a collection which is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have keys and values.

A dictionary is an associative array (also known as hashes). Any key of the dictionary is associated (or mapped) to a value. 
The values of a dictionary can be any Python data type. 
So dictionaries are unordered key-value-pairs. ... Dictionaries belong to the built-in mapping type.

A dictionary maps a set of objects (keys) to another set of objects (values). 
A Python dictionary is a mapping of unique keys to values. 
Dictionaries are mutable, which means they can be changed. 
The values that the keys point to can be any Python value. 
Dictionaries are unordered, so the order that the keys are added doesn't necessarily reflect what order they may be reported back.


#create dictionary

mydict = dict(name="Guhan",age=28,mobile=979181,email="raghavaguhan@gmail.com")
print(mydict)

Result:-
{'name': 'Guhan', 'age': 28, 'mobile': 979181, 'email': 'raghavaguhan@gmail.com'}


details ={
           'name':"Guhan",
            'age':27,
            'mobile':698698,
            "address":{
                "No":123,
                "Street":"South"
            },


}
print(details)
print(details['name'])
print(details['address'])
print(details["address"]["Street"])

#Sorted Dict

for key, value in sorted(mydict.items()):
    print(key, value)

Result:-
age 28
email raghavaguhan@gmail.com
mobile 979181
name Guhan


#Sort by key

print(sorted(details.keys()))

for key in sorted(details):
    print(key, details[key])

keylist = details.keys()
print(keylist)
# dict_keys(['name', 'age', 'mobile', 'address'])

L=list(details)
print(L)
print(sorted(L))

# Sorted by values

data = {
         "price2":1288,
         "price1":2388,
          "price3":35355
}
print(sorted(data.values()))
x=sorted(data.values())

for value in range(0, len(x)):
     print(x[value])

x=sorted(data, key=data.__getitem__)
print(x)

x=[value for (key, value) in sorted(data.items())]
print(x)

x=sorted(data, key=data.__getitem__, reverse=True)
print(x)

print(sorted(data, key=str.lower))


Result:

{'name': 'Guhan', 'age': 27, 'mobile': 698698, 'address': {'No': 123, 'Street': 'South'}}
Guhan
{'No': 123, 'Street': 'South'}
South
['address', 'age', 'mobile', 'name']
address {'No': 123, 'Street': 'South'}
age 27
mobile 698698
name Guhan
dict_keys(['name', 'age', 'mobile', 'address'])
['name', 'age', 'mobile', 'address']
['address', 'age', 'mobile', 'name']
[1288, 2388, 35355]
1288
2388
35355
['price2', 'price1', 'price3']
[2388, 1288, 35355]
['price3', 'price1', 'price2']
['price1', 'price2', 'price3']
