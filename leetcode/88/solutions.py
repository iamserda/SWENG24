def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    nums1_indexer = m - 1
    nums2_indexer = n - 1
    next_indexer = m + n - 1

    while next_indexer >= 0:
        if nums1[nums1_indexer] >= nums2[nums2_indexer]:
            nums1[next_indexer] = nums1[nums1_indexer]
            nums1_indexer -= 1
        else:
            nums1[next_indexer] = nums2[nums1_indexer]
            nums2_indexer -= 1
        next_indexer -= 1
        if nums1_indexer < 0 or nums2_indexer < 0:
            break


# Testing:
nums1 = [1]
nums2 = []
M = 1
N = 0
print(f"Before: {nums1}")
merge(nums1=nums1, m=M, nums2=nums2, n=N)
print(f"After: {nums1}")
