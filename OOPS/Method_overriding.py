#Method Overriding
class Payilagam:
        def teach(self,name):
         print(name)
obj = Payilagam()
obj.teach("Muthu")

class Branch(Payilagam):
      def teach(self,name,age):
          print(name,age)
branch = Branch()
branch.teach("Guhan",28)


Result:

Muthu
Guhan 28
