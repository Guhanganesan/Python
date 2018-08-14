class Training:
  def __init__(self, name, friend, age):
       self._public=name
       self._protected=friend
       self._private=age
  def getValues(self):
      print(self._public)
      print(self._protected)
      print(self._private)
obj = Training("Muthu","Guhan",32)
#obj.getValues()
print(obj._private)

class Branch(Training):
       def check(self):
           print(self._public)
           print(self._protected)
           print(self._private)
obj1 = Branch(2,3,4)
#print(obj1.getValues())
obj1.check()
print(obj1._private)

Result:-

32
2
3
4
4
