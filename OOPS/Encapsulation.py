#Encapsulation
class Rbi:
    _area="Chennai" #protected 
    __mob=768767    #private
    def __init__(self):
        self.__pin=12345
        self.name="RBI"
        print(self.__mob, self._area)
    def getValues(self):
        print(self.name, self.__pin)
    
    def __rate(self): 
        print("Rate is 10%")
    def add(self):
        self.__rate()

#obj=Rbi()
#obj.getValues()
#print(obj.area)
#print(obj.__mob) #AttributeError: 'Rbi' object has no attribute '__mob'
#obj.add()
#obj.__rate() #AttributeError: 'Rbi' object has no attribute '__rate'


class MyBank(Rbi):
     def __init__(self):
        print(self._area)
        #print(self.__mob) #cannot print
        self.add()
        #self.__rate()


obj=MyBank()
print(obj._area)

----------------------------------------------------------------------------------------------
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

#---------------------------------------------------------------

class Periyar:
      __name="Priyar"
      def add(self):
          print("Add")

      def __getValues(self):
          print("Get Values")
          self.__name
obj = Periyar()
obj.add()
obj.__name # cannot call private

#--------------------------------------------------------------
#Abstract base class
import abc
class AbstractAnimal(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def walk(self):
        ''' data '''

    @abc.abstractmethod
    def talk(self):
        ''' data '''

class Duck(AbstractAnimal):
    name = ''

    def __init__(self, name):
        print('duck created.')
        self.name = name

    def walk(self):
        print('walks')

    def talk(self):
        print('quack')

obj = Duck('duck1')
obj.talk()
obj.walk()






