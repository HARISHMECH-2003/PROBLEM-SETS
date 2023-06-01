def longest_word_length(words):
    longest_length=0
    for word in words:
        if len(word)>longest_length:
            longest_length=len(word)
    return longest_length