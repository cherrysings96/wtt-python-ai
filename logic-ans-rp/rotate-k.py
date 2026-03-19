# Write a Python program to rotate a list to the right by k positions.
# Example:
# Input:  [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

def rotate_right(lst, k):
    # Handle cases where k is greater than the length of the list
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


# Example usage
input_list = [1, 2, 3, 4, 5]
k = 2

result = rotate_right(input_list, k)

print(result)  # Output: [4, 5, 1, 2, 3]
