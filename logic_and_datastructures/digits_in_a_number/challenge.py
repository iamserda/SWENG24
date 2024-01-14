"""
Given some integer x, print each digit within the integer.
constraint: you cannot convert the integer to any other data types.
"""
import random


def digit_in_number(num: int) -> None:

    if num is None or not isinstance(num, int):
        print(TypeError(f"Error: Expected argument of type 'int'.\
            received {type(int)}"))
    result = []
    print(f"Number: {num}")
    while num > 0:
        result.append(num % 10)
        num = int(num / 10)
    result.reverse()
    return result


print(*digit_in_number(random.randrange(10**6, 10**7-1)))
