try:
    user = int(input("Enter Value"))
    assert(user>0)
    print(user+100)

except AssertionError:
    print("Ur data is not suitable for this process")
    
    
Result:-

Enter Value -10
Ur data is not suitable for this process
