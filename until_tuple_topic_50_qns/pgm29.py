def vowels(s):
    count = 0
    for ch in s:
        if ch in "AEIOUaeiou":
            count += 1
    return count


print(vowels("Malayalam"))
