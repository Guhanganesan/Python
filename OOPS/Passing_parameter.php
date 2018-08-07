class Training:
   def teach(self,work):
          print(work)
   def __init__(self,name): #It will call first
          print(name)
obj = Training("He is Mr.Guhan")
obj.teach("He conducts python course")


Result:

He is Mr.Guhan
He conducts python course
