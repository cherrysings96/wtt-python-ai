# # Write a function that returns True if a string is a palindrome without using slicing.
# def is_palindrome(s):
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True


# # Example usage:
# print(is_palindrome("racecar"))  # Output: True
# print(is_palindrome("hello"))    # Output: False
