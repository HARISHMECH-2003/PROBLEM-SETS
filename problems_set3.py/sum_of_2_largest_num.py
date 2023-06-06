def sum_two_largest_numbers(numbers):
    sorted_numbers = sorted(numbers,reverse=True)
    return sorted_numbers[0] + sorted_numbers[1]

numbers=[23,22,33,56,47,35]
result=sum_two_largest_numbers(numbers)
print(result)