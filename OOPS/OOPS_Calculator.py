# Simple Inheritance example
class Calculator:
    def add(self,x,y):
        return  x+y
    def sub(self,x,y):
        return  x-y
    def mul(self,x,y):
        return x*y
siva = Calculator()
print(siva.add(20,30))

class Child(Calculator):
    def ex(self):
        pass

child = Child()
print(child.add(100,200))
print(child.sub(200,100))
print(child.mul(30,20))

Result:
50
300
100
600
