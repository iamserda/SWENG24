## WRITE THE PRINT_ITEMS FUNCTION HERE ##
def linear_time(n):
    """showing an example of linear-time complexity"""
    for i in n:
        print(f"Number: {i}")


def still_linear_time(n):
    """showing an example of linear-time complexity"""
    for idx in n:
        print(f"Number: {idx}")

    for jdx in n:
        print(f"Number: {jdx * jdx}")


# DO NOT CHANGE THIS LINE:
linear_time(range(10))
still_linear_time(range(10))
