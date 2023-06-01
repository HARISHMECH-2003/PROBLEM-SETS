def div_by_num(number):
    if number/3==0:
        print("Three")
    elif number/5==0:
        print("Five")
    elif number/3==0 and number/5==0:
        print("Three and Five")
    else:
        return number
