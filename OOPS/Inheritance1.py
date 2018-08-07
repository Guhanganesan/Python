class Training:
   def teach(self,work):
          print(work)
   def __init__(self,name): #It will call first
          print(name)
obj = Training("He is Mr.Guhan")
obj.teach("He conducts python course")


class Developing(Training):
       def __init__(self,name):
           print(name)
       def dev(self,work):
              print(work)
obj1 = Developing("He is Mr.Siva")
obj1.dev("He is developing android app")

Result:
He is Mr.Guhan
He conducts python course
He is Mr.Siva
He is developing android app
