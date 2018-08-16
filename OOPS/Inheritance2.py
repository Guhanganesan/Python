class SivaKumar:
    def __init__(self,name,age,mob):
            self.name=name
            self.age=age
            self.mob=mob
    def act(self,age):
        print(self.name)
        print(age)

siva = SivaKumar("Kumar",23,731631)
siva.act(34)

class Karthik(SivaKumar):
     def dance(self):
         print(self.name)

obj= Karthik("Karthik",45,9883269823)
obj.dance()


class Surya(SivaKumar):
    def drive(self):
        print(self.name)
        print(self.age)
        print(self.mob)

surya = Surya("Surya",33,67869)
surya.drive()

class Dev(Surya):
    def drawing(self,color):
        print(color)
        print(self.name)
        print(self.mob)
    def drive(self):
        print()
dev = Dev("Devendra",12,63987)
dev.drawing("pink")

Result:-
Kumar
34
Karthik
Surya
33
67869
pink
Devendra
63987









