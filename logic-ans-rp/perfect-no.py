# Check if a Number is Perfect
# Write a Python program to check whether a given number is a perfect number.
# A perfect number is equal to the sum of its proper divisors (excluding itself).
# Example:
# Input:  6
# Output: True
def is_perfect_number(n):
    if n < 2:
        return False  # Perfect numbers are greater than 1

    divisors_sum = 1  # Start with 1, which is a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Add the complementary divisor if it's different
                divisors_sum += n // i

    return divisors_sum == n


# Example usage
number = 6
result = is_perfect_number(number)
print(result)  # Output: True
number = 28
result = is_perfect_number(number)
print(result)  # Output: True
number = 12
result = is_perfect_number(number)
print(result)  # Output: False
