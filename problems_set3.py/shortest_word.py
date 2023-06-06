def shortest_word(string):
    words=string.split()
    shortest_word=min(words, key=len)
    return len(shortest_word)

string="Harish from mechanical dept second year"
result=shortest_word(string)
print(result)