#Encapsulation
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
obj.getValues()

Result:-

Muthu
Guhan
32
