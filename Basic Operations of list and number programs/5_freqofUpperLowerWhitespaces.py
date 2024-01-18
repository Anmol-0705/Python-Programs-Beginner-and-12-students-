s=input("Enter the String")
# cap=s.upper()
# low=s.lower()
# print(cap)
freq=0
white_freq=0
low_freq=0
for char in s:
    if(char.isupper()):
        freq+=1
    elif(char.isspace()):
        white_freq+=1
    elif(char.islower()):
        low_freq+=1

print(f"The Frequency of UpperCase are {freq}")
print(f"The Frequency of LowerCase are {low_freq}")
print(f"The Frequency of WhiteSpaces are {white_freq}")
