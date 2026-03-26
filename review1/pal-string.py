def pal(s):
    rev = s[::-1]
    if rev == s:
        return "palindrome"
    else:
        return "not"


s = input("Enter the string:")
ans = pal(s)
print(ans)
