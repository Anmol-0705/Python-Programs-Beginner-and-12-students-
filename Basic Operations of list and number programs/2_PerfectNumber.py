def is_perfect_number(num):
    if num <= 0:
        return False

    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == num

# Example usage:
number_to_check = int(input("Enter a number to check for perfection: "))
if is_perfect_number(number_to_check):
    print(f"{number_to_check} is a perfect number.")
else:
    print(f"{number_to_check} is not a perfect number.")
