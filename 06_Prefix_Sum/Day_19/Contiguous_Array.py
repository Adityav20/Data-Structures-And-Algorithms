#https://leetcode.com/problems/contiguous-array/description/
"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Example 3:
Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
"""
from collections import defaultdict

def findMaxLength(nums):
    zero = 0
    one = 0
    f = defaultdict(int)
    ans = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zero += 1
        else:
            one += 1
        diff = zero - one
        if diff == 0:
            ans = max(ans, i+1)
            continue
        if diff not in f:
            f[diff] = i
        else:
            idx = f[diff]
            length = i - idx
            ans = max(length,ans)

    return ans

nums1 = [0,1]
nums2 = [0,1,0]
nums3 = [0,1,1,1,1,1,0,0,0]

print(findMaxLength(nums1))
print(findMaxLength(nums2))
print(findMaxLength(nums3))