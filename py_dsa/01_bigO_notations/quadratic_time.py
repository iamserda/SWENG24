## WRITE THE PRINT_ITEMS FUNCTION HERE ##
def quadratic_time(n):
    """showing an example of linear-time complexity"""
    count = 0
    for idx in range(n):
        for jdx in range(n):
            count += 1
            print(f"Count: {idx}{}")


# DO NOT CHANGE THIS LINE:
quadratic_time(n=10)
