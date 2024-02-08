# Solution 1: Two Sum

## Intuition

The problem requires finding two numbers in a list that add up to a given target. One approach is to iterate through the list and for each element, check if its complement (the target minus the current element) exists in the list. 

## Approach

We can use a dictionary to store the complements of each element as we iterate through the list. This allows us to quickly check if the complement of the current element exists in the dictionary, indicating that we've found a pair that sums up to the target.

## Complexity

- Time complexity: 
  - The time complexity of this approach is O(n) because we iterate through the list once, where n is the number of elements in the list.

- Space complexity:
  - The space complexity is also O(n) because in the worst-case scenario, we might store all elements in the complements dictionary.

## Code

```python
class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in complements:
                return [complements[complement], index]
            complements[value] = index
```
