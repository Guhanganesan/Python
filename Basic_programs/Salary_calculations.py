salary = input("Enter salary")
salary = int(salary)
bonus=0
total_salary=0
if salary<0:
    print("Not valid amount")

elif salary<5000 and salary>0:
    bonus=0.05
    total_salary=salary+salary*bonus
    print(total_salary)

elif salary>5000 and salary<=10000:
    bonus = 0.1
    total_salary = salary + salary * bonus
    print(total_salary)
elif salary >10000 and salary<=20000:
    bonus = 0.2
    total_salary = salary + salary * bonus
    print(total_salary)
else:
    bonus = 0.3
    total_salary = salary + salary * bonus
    print(total_salary)
    
Result:

Enter salary-1000
Not valid amount

Enter salary1000
1050.0

Enter salary6000
6600.0

Enter salary12000
14400.0

Enter salary22000
28600.0

