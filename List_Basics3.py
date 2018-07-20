#Create List
value=0
L=[]
while value>=0:
    x = int(input("Enter values"))
    L=L+[x]
    print(L)
    
 Result:
    Enter values10
    [10]
    Enter values12
    [10, 12]
    Enter values13
    [10, 12, 13]
    Enter values15
    [10, 12, 13, 15]
    Enter values
    
  #Using function

    def cal():
        value=0
        L=[]
        while value>=0:
            x = int(input("Enter values"))
            L=L+[x]
            print(L)
    cal()
    
    Result:
        Enter values12
        [12]
        Enter values13
        [12, 13]
        Enter values
  
#Return the values

def cal():
    value=0
    L=[]
    while value>=0:
        x = int(input("Enter values"))
        L=L+[x]
        return L

def main():
       new_list=cal()
       print(new_list)
main()
        
 Result:
    
    Enter values12
    [12]
    
# Call function in another function

#Return the values
def cal():
    value=0
    L=[]
    while value>=0:
        x = int(input("Enter values"))
        L=L+[x]
        return L

x=[0]
def main():
        x=cal()
        print(x)
main()

Result:
    Enter values23
    [23]
    
   
    
        
        
        

    
    
    
    
    
