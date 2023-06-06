def reverse_digits(number):
    if number==0:
        return [0]
    digits=[]
    while number>0:
        digit=number%10
        digits.append(digit)
        number=number//10
    return digits

number=2345
result=reverse_digits(number)
print(result)