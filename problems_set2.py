def process_data(datas):
    result=1
    for sublist in datas:
        calc_value=sublist[0]-sublist[1]
        result=result*calc_value
    return result

datas=[[2,3],[3,5],[5,2]]
output=process_data(datas)
print(output)
