## WRITE THE PRINT_ITEMS FUNCTION HERE ##
def quadratic_time(search_list, search_item):
    """showing an example of quadratic-time complexity"""
    print("Searching for:", search_item)
    print("List:", search_list)
    start = 0
    end = len(search_list) - 1
    while start < end:
        mid = (end + start) // 2
        print(mid)
        if search_list[mid] == search_item:
            return mid
        if search_item > search_list[mid]:
            start = mid + 1
            continue
        end = mid - 1
        print(start, mid, end)
    return -1


# DO NOT CHANGE THIS LINE:
n = list(range(0, 101, 5))
print(quadratic_time(n, 80))
print(quadratic_time(n, 180))
print(quadratic_time(n, -1))
