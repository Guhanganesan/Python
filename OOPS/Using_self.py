class Training:

  def __init__(self):
       self.name="Guhan"
       self.friend="Muthu Ramalingam"
       self.age=28

obj = Training()


class Developing(Training):
     def  getValues(self):
         print(self.name)
         print(self.age)
         print(self.friend)
obj1= Developing()
obj1.getValues()

Result:

Guhan
28
Muthu Ramalingam
