# Write a Python program to count how many numbers in a given list have an even number of digits.
# Example:
# Input:  [12, 345, 2, 6, 7896]
# Output: 2

def count_even_digit_numbers(lst):
    count = 0
    for num in lst:
        if len(str(num)) % 2 == 0:
            count += 1
    return count


# Example usage
input_list = [12, 345, 2, 6, 7896]
result = count_even_digit_numbers(input_list)
print(result)  # Output: 2
