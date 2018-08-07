class Training:
   area="200sft"
   def teach(self,work):
          print(work)
   def __init__(self,name): #It will call first
          print(name)
obj = Training("He is Mr.Guhan")
obj.teach("He conducts python course")

class Developing(Training):
       time="2 Hour"
       def __init__(self,name):
           print(name)
       def dev(self,work):
              print(work)
obj1 = Developing("He is Mr.Siva")
obj1.dev("He is developing android app")

class Project(Developing):
    def run(self):
        print("In Progress")
project=Project(100)
project.dev("Project work is in process")
project.teach("Taking classes")
project.run()
print(project.time)
print(project.area)

Result:-
He is Mr.Guhan
He conducts python course
He is Mr.Siva
He is developing android app
100
Project work is in process
Taking classes
In Progress
2 Hour
200sft
