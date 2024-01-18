n=int(input("Enter the number "))
m=n
count=0
cube=0
while(n!=0):
    d=n%10
    count+=1
    n=n//10
n=m
while(n!=0):
    d=n%10
    cube=cube+d**count
    n=n//10
if(cube==m):
    print("Armstrong Number")
else:
    print("It is not a Armstrong number")
