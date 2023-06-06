def better_than_peers(score,my_score):
    average_score=sum(score)/len(score)
    return my_score > average_score

test_score=[78,89,56,78,90]
my_score=87
result=better_than_peers(test_score,my_score)
print(result)