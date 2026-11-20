# Count vowels and consonants in a string.

s = "Alice"


def isvowel():
    count = 0
    for ch in range(0, len(s)):
        if s[ch] in "AEIOUaeiou":
            count += 1
    return count


c = isvowel()
print(f"No. of vowels in {s} is {c}")
print(f"No. of consonents in {s} is {len(s)-c}")
