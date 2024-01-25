# Quadratic Time Complexity or O(N^2)

Quadratic time complexity occurs when our code can be expected
to complete `n x n` or `n**2` operations.

```python
## WRITE THE PRINT_ITEMS FUNCTION HERE ##
def quadratic_time(n):
    """showing an example of linear-time complexity"""
    count = 0
    for idx in range(n):
        for jdx in range(n):
            count += 1
            print(f"Count: {idx}{jdx}")


# DO NOT CHANGE THIS LINE:
quadratic_time(n=5) # 25 outputs or 5 x 5.
quadratic_time(n=10) # 100 outputs or 10 x 10.
```
Quadratic Time-Complexity is the cut-off when,
we always want to do better than quadratic time complexity wi