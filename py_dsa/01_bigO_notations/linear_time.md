# Linear Time or O(n) where n is the input size(len)

```python
# */linear_time.py
def linear_time(n):
    for i in range(n):
        print(f"Number: {i}")
linear_time(2)
```

RUN in bash `$ python3 -u linear_time.py`

```bash 
Number: 0
Number: 1
```

```python
# */linear_time.py
def linear_time(n):
    for i in range(n):
        print(f"Number: {i}")
linear_time(5)
```

RUN in bash `$ python3 -u linear_time.py`

```bash
Number: 0
Number: 1
Number: 2
Number: 3
Number: 4
```

This 'linear_times' function performs its routine in O(n) or 'Linear Time Complexity" because the number of 'print()' operations we complete is PROPORTIONAL to the number of inputs.

It does not mean the same. For example, if we printed twice, the number of operations would be 2 x n, however it would still be proportional to n. So for any x number of operations to be done with this function, the size of n decides how many times we repeat these operations.
`f(5) = 2ops x n = 2ops x 5 = 10ops.`
`f(10) = 2ops x n = 2ops x 10 = 20ops.`

By doubling 'n' inputs, we completed double the tasks or ops.

As n gets larger, 1M or 10M operations,
the size of n is the most important value
driving the number of operations.
Hence, we drop constants. 
`O(10 x n)` becomes `O(n)`.


**Example**:

```python
def still_linear_time(n):
    """showing an example of linear-time complexity"""
    for idx in n:
        # O(n)
        print(f"Number: {idx}")

    for jdx in n:
        # O(n)
        print(f"Number: {jdx * jdx}")
```

O(n) + O(n) == O(n + n) == O(2n) == O(n), in Big O notations we only care
about the driver. The value that has a significant impact on code efficiency.
Here it is n. As n gets larger, we need to complete more loop cycles.
Therefore, 2 x n, as n goes towards infinity is like 2 x infinity, its infinity.
So 2 x n, as n -> +inf is n.

Here, we complete n operations. This would also remain true if we were completing 10xn operations.

O(10 x n)... is regarded as in-line with O(n). 
Meaning, any constant K, here K is 10, times our input size 'n' should be dropped.
