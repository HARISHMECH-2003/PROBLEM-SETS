def playing_banjo(name):
    if name[0].lower()=='r':
        return "you are playing bunjo"
    else:
        return "you are not playing bunjo"
    
name1="harish"
name2="RONALDO"
result1=playing_banjo(name1)
result2=playing_banjo(name2)
print(result1)
print(result2)