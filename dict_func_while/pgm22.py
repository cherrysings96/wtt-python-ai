# return longest word in a sentence
sentence = "This is a long preposterous sentence"
word = sentence.split()


def long_word():
    global sentence
    global word
    longest_word = ""
    for w in word:
        if len(w) > len(longest_word):
            longest_word = w
    return longest_word


print(long_word())
