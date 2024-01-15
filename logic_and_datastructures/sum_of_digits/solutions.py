def sum_of_digits(some_number):
    sum = None
    if isinstance(some_number, int):
        sum = 0
        while some_number != 0:
            remainder_num = some_number % 10
            some_number = some_number // 10
            sum += remainder_num
    print(sum)
    return sum


assert sum_of_digits(12345) == 15
assert sum_of_digits(1) == 1
assert sum_of_digits(345) == 12
assert sum_of_digits(0) == 0
