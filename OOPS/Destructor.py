class Training:
  def __init__(self):
       self.name="Guhan"
       self.friend="Muthu Ramalingam"
       self.age=28
  def getValues(self):
      print(self.name)
      print(self.friend)
  def __del__(self):
      print("Destructor Started")
  def getAgainValues(self):
      print(self.name)
      print(self.friend)
obj = Training()
obj.getValues()
obj.getAgainValues()

Result:
Guhan
Muthu Ramalingam
Guhan
Muthu Ramalingam
Destructor Started
