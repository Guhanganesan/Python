#Functions Exercise
#1.

def sum(n):
    s=0
    while n > 0:
        s += 1
        n -= 1
    return s
m=sum(6)
print(m)

#.2
val=4
for i in range(val, 0, -1):
    print(i)

#.3
val=4
for i in range(4,-1, -1):
    print(i)


#.Average for 5 numbers

def main():
    sum=0.0
    x=int(input("Enter how many numbers"))
    for i in range(1,x+1):
         num = eval( input("Enter Number: "+ str(i)+ ": "))
         sum = sum+num
    avg=sum/5
    print(avg)
main()



Result:

6
4
3
2
1
4
3
2
1
0
Enter how many numbers5
Enter Number: 1: 12
Enter Number: 2: 13
Enter Number: 3: 14
Enter Number: 4: 15
Enter Number: 5: 16
14.0


