 
#that calc.py module, i have added in my library,
#ImportError
try:
    import calc1
    a=10
    b=2
    print("Open")
    print(calc1.div(a,b))
   
except ZeroDivisionError as e1:
    print("U cannot divide a number by zero bcz:", e1)

except ModuleNotFoundError as e2:
    print("Module is not found",e2)

finally:  
    print("Close") 


