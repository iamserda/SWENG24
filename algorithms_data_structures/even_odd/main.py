def is_even(some_number):

    if not isinstance(some_number, int):
        raise TypeError("Error: input is not an integer...")
    return True if some_number % 2 == 0 else False


# Test:
number = -5
print(number, "Even" if is_even(number) else "Odd")
number = 4
print(number, "Even" if is_even(number) else "Odd")
