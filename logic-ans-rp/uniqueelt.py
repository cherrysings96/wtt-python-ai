# Write a Python program to find the element that appears only once in a list where all other elements appear exactly twice.
# Example:
# Input:  [2, 3, 5, 4, 5, 3, 2]
# Output: 4

def find_unique_element(lst):
    unique_element = 0
    for num in lst:
        unique_element ^= num  # XOR operation will cancel out duplicates
    return unique_element


# Example usage
input_list = [2, 3, 5, 4, 5, 3, 2]
result = find_unique_element(input_list)
print(result)  # Output: 4
