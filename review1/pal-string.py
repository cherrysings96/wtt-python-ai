def pal(s):
    l = s.lower()
    rev = l.reverse()
    if s == rev:
        print("Palindrome")
    else:
        print("Not palindrome")


s = input("Enter the string:")
pal(s)
