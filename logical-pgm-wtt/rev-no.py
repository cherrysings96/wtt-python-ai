# reverse of a number
def reverse_number(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
    return reverse


number = 12345
reverse = reverse_number(number)
print(f"The reverse of {number} is {reverse}")
