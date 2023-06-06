def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]

numbers=[23,22,33,56,47,35]
result=sum_two_smallest_numbers(numbers)
print(result)