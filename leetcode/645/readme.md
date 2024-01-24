# 645. Set Mismatch

## Problem Description

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

## Examples

**Example 1:**

Input: `nums = [1,2,2,4]`
Output: `[2,3]`

**Example 2:**

Input: `nums = [1,1]`

Output: `[1,2]`

## Constraints

`2 <= nums.length <= 104`

`1 <= nums[i] <= 104`

## Time Complexity

- What is the time complexity of your solution?
  - O(n log n) because of the TimSort algorithm being used to sort the nums list(aka array).

- Can you improve the time complexity? How?
  - Yes, I could instead use a hashtable to find the duplicate values in O(n). Keys are the elements of the nums list. Indices would be stored within list as the value-pair to each key. Therefore, any list with length more than 1 is the repeated element. I would need to iterate over the dictionary in order to get these values which has an O(n) worst case but it won't increase Time Complexity. O(n) is still better than O(n log n).

- What is the space complexity of your solution?
- Technically O(2n) because we are creating new sets, which boils down to O(n)

- Can you improve the space complexity? How?
- Yes, I learned on LeetCode solutions that 
we do not need to use extra time or space on LeetCode.
This can be done in O(1) for both time and space using 
algebraic reasoning. Instead, people use mathematical 
reasonings to solve this based on the sum of the values 
in the set vs the sum of the values that should have been there to find the missing item.

For example, [1,2,2,4] has a sum of 9. 

The sum(set[1,2,2,4]) is 7, so 2 is the repeated value. [2,]

To find the missing value, we need the sum of all values that should be there for a list of len(range(1, len([1,2,2,4])+1)) which is 10 == sum([1,2,3,4]). Now, the sum([1,2,3,4]) aka 10 - sum(set[1,2,2,4]) aka 7 is 3. Therefore we found [2, 3] and return that. Time/Space complexities are CONSTANT!

This solution is by LeetCoder [Stefan Pochmann](https://leetcode.com/StefanPochmann/).
His elegant solution can be found under the solutions list on LeetCode for problem 645...
