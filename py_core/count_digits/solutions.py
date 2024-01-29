"""Given a number, returns the number of digits in num"""


def count_digits(num):
    """Given a number, returns the number of digits in num"""
    arr = []
    while abs(num) > 0:
        arr.append(abs(num) % 10)
        num = int(num / 10)
    return len(arr)


# TESTS ARENA:
# DO NOT MAKE ANY CHANGE TO THE CODE BELOW...
assert count_digits(-12345) == 5
assert count_digits(1234) == 4
assert count_digits(-45) == 2
assert count_digits(4) == 1
