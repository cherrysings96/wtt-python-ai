# Write a Python program to check whether a list is monotonic (entirely increasing or decreasing).
# Example:
# Input:  [1, 2, 2, 3] → Output: False
# Input:  [5, 4, 3]   → Output: True

def is_monotonic(lst):
    # If the list has 0 or 1 items, it's technically monotonic
    if len(lst) <= 1:
        return True

    increasing = decreasing = True

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        elif lst[i] < lst[i - 1]:
            increasing = False
        else:
            # If they are equal, it's not strictly increasing or decreasing
            return False

    return increasing or decreasing


# Example usage
print(is_monotonic([1, 2, 2, 3]))  # Output: False
print(is_monotonic([5, 4, 3]))     # Output: True
