# Write a Python program to rearrange the elements of a list in zig-zag fashion such that:
# a < b > c < d > e < f ...
# Example:
# Input:  [4, 3, 7, 8, 6, 2, 1]
# Output: [3, 7, 4, 8, 2, 6, 1]


def zig_zag(arr):
    for i in range(len(arr) - 1):
        if i % 2 == 0:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


# Example usage
input_list = [4, 3, 7, 8, 6, 2, 1]
result = zig_zag(input_list)
print(result)  # Output: [3, 7, 4, 8, 2, 6, 1]
