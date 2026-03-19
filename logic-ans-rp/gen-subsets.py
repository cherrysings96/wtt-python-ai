# Generate All Subsets (Power Set)
# Write a Python program to generate all possible subsets of a given list.
# Example:
# Input:  [1, 2, 3]
# Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

def generate_subsets(lst):
    subsets = [[]]  # Start with the empty subset

    for num in lst:
        # For each number, add it to existing subsets to create new subsets
        new_subsets = [curr + [num] for curr in subsets]
        subsets.extend(new_subsets)

    return subsets


# Example usage
input_list = [1, 2, 3]
result = generate_subsets(input_list)
print(result)  # Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
