"""
Given some integer x, print each digit within the integer.
constraint: you cannot convert the integer to any other data types.
"""

def digit_in_number(num: int) -> None:
    """Prints each digit within the given integer 'num' arg."""
    if isinstance(num, int):
        result = []
        while num >= 0:
            result.append(num % 10)
            num = num // 10
        result.reverse()
        return result
    # RAINY DAY
    raise TypeError(
        f"Error: Expected argument of type 'int'. Received type: {type(num)}")


numbers = digit_in_number(1)
print(numbers)
