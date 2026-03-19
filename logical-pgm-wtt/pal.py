# reverse of no. has to be the same as the original number
# turn number into string, reverse the string, and if it is the same as the original string
# it is a palindrome
# 121,131,454

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]


number = 121
if is_palindrome(number):

    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
