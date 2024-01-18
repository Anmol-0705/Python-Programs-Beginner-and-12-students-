# def seq(lst):
#     last_num = seq[-1]
#     divisors = [i for i in range(1, last_num + 1) if last_num % i == 0]
#     print(divisors)
# def main():
#     seq(int(input()))

# if __name__=="__main__":
#     main()


# def print_divisors(seq):
#     last_num = seq[-1]
#     divisors = [i for i in range(1, last_num + 1) if last_num % i == 0]
#     print(divisors)

def print_divisors_of_last(numbers):
    if not numbers:
        print("No numbers provided.")
        return

    last_number = numbers[-1]

    if not isinstance(last_number, int):
        print("The last input must be an integer.")
        return

    divisors = [i for i in range(1, last_number + 1) if last_number % i == 0]

    print(f"Divisors of the last number ({last_number}): {divisors}")

# Example usage:
try:
    input_numbers = list(map(int, input("Enter a sequence of numbers separated by spaces: ").split()))
    print_divisors_of_last(input_numbers)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
