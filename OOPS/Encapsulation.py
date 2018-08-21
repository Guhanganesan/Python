class Periyar:
      def add(self):
          print("Add")

      def __getValues(self):
          print("Get Values")
obj = Periyar()
obj.add()
#obj.__getValues() Can not access private method

class Anna:
     def __init__(self):
          self.__getValue() # call private method within the class
     def __getValue(self):
         print("get values here")
obj1 = Anna()

Result:-
Add
get values here


