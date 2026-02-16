word = str(input("Enter a word:"))


def vowelnumber(word):
    count = 0
    for ch in word:
        if ch in "AEIOUaeiou":
            count += 1
    return count


print(vowelnumber(word))
