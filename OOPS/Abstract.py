Abstract classes are classes that contain one or more abstract methods. 
An abstract method is a method that is declared, but contains no implementation.
Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods. 
Subclasses of an abstract class in Python are not required to implement abstract methods of the parent class.


Program:

class Siva:
    def act(self):
        pass
    def dance(self):
        pass
    def yoga(self):
        print("Doing yoga practice")



class Surya(Siva):

     def act(self):
         print("He is acting")
     def chack(self):
         super().yoga()
obj = Surya()
obj.chack()
obj.act()

Result:

Doing yoga practice
He is acting

