#https://leetcode.com/problems/max-consecutive-ones-iii/description/
"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""
from collections import defaultdict

def longestOnes(nums, k):
    f = defaultdict(int)
    low,high = 0, 0
    res = 0
    while(high<len(nums)):
        f[nums[high]] += 1 #HashMap
        length = high - low + 1
        max_freq = max(f.values())
        diff = length - max_freq
        while(diff>k):
            f[nums[low]] -= 1
            if f[nums[low]] < 1: #del char from HP which has 0 count
                del f[nums[low]]
            low += 1
            length = high - low + 1
            max_freq = max(f.values())
            diff = length - max_freq
        res = max(res, length)
        high += 1

    return res if res != 0 else -1

nums1 = [1,1,1,0,0,0,1,1,1,1,0]
k1 = 2

nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k2 = 3

print(longestOnes(nums1, k1))
print(longestOnes(nums2, k2))