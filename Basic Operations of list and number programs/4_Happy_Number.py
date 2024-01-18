def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

number_to_check = int(input("Enter a number to check for happiness: "))
if is_happy_number(number_to_check):
    print(f"{number_to_check} is a happy number.")
else:
    print(f"{number_to_check} is not a happy number.")
