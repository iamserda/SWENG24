def is_even(some_number):
    if not isinstance(some_number, int):
        print(TypeError(f"Error: Expected 'int' received {type(some_number)}"))
    return "Even" if some_number % 2 == 0 else "Odd"


# Test:
number = -5
print(str(number)+":", is_even(number))
number = 4
print(str(number)+":", is_even(number))
# number = "3"
# print(str(number)+":", is_even(number))
