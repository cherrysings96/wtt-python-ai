# Write a Python program to find all pairs of elements in a list such that the absolute difference between them is equal to a given number k.
# Example:
# Input:  lst = [1, 5, 2, 2, 7, 5], k = 3
# Output: [(5,2), (2,5)]
def find_pairs_with_diff(lst, k):
    pairs = []
    # Use a set to keep track of values we've already used as the 'first' number
    seen_first = set()

    for i in range(len(lst)):
        if lst[i] in seen_first:
            continue  # Skip if we already found pairs for this number

        for j in range(i + 1, len(lst)):
            if abs(lst[i] - lst[j]) == k:
                pairs.append((lst[i], lst[j]))
                seen_first.add(lst[i])
                break  # Move to the next unique number once a pair is found
    return pairs


input_list = [1, 5, 2, 2, 7, 5]
k = 3
print(find_pairs_with_diff(input_list, k))
# Output: [(5, 2), (2, 5)]
