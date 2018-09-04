from collections import OrderedDict

#same key will override the previous key

details=OrderedDict([('name','Guhan'),('age',28),('name','anbu'),('mobile',87678)])
print(details)
for i,j in details.items():
    print(i,j)
    
Result:-
OrderedDict([('name', 'anbu'), ('age', 28), ('mobile', 87678)])
name anbu
age 28
mobile 87678



