def additive_inverse(numbers):
    inverse_num=[]
    for num in numbers:
        inverse_num.append(-num) 
    return inverse_num
numbers=[-1,2,-3,4,-5]
result=additive_inverse(numbers)
print(result)
