def pal(x, temp, rev):
    while (temp != 0):
        dig = temp % 10
        rev = rev*10+dig
        temp = temp//10

    if (x == rev):
        return "Palindrome"
    else:
        return "Not palindrome"


print(pal(121, 121, 0))
