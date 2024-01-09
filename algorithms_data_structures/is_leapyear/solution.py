def is_leap_year(number):
    if not isinstance(number, int):
        raise TypeError("Error: not an integer...")
    if number % 4 == 0:
        if number % 400 == 0:
            return True
        if number % 100 == 0:
            return False
        return True


print(1900, is_leap_year(1900))
