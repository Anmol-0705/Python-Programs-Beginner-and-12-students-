# Logic 1 in this it is inputted as string so slicing can be done.
# n=(input("Enter the number"))
# m=n
# x=n[::-1]
# if(m==x):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# logic 2 in this usual logic will be used.

n=int(input("Enter the number "))
m=n
rev=0
while(n!=0):
    d=n%10
    n=n//10 # This will ingnore the extra decimals (floor division)
    rev=rev*10+d
print("The Reversed Number is ",rev) # To verify the reverse of the number

if(m==rev):
    print("Palindrome")
else:
    print("It is not palindrome")


