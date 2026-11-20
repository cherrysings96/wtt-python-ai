# Write a Python program to count the number of uppercase and lowercase letters in a given string.
# Example:
# Input:  "Hello World!"
# Output: Uppercase: 2, Lowercase: 8
def count_upper_lower(s):
    uppercase_count = 0
    lowercase_count = 0

    for char in s:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


# Example usage
input_string = "Hello World!"

upper_count, lower_count = count_upper_lower(input_string)
print(f"Uppercase: {upper_count}, Lowercase: {lower_count}")  #
# Output: Uppercase: 2, Lowercase: 8
