#https://leetcode.com/problems/subarray-sum-equals-k/description/
"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""
from collections import defaultdict

def subarraySum(nums, k):
    total = 0
    ans = 0
    f = defaultdict(int)
    f[0] = 1  # Empty prefix sum

    for i in range(len(nums)):
        total = total + nums[i]
        freq = f[total - k]
        ans += freq
        f[total] += 1  # Update hashmap

    return ans


nums1 = [1,1,1]
k1 = 2

nums2 = [1,2,3]
k2 = 3

nums3 = [1,-1,0]
k3 = 0

print(subarraySum(nums1, k1))
print(subarraySum(nums2, k2))
print(subarraySum(nums3, k3))