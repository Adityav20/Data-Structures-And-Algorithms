#https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
def minSubArrayLen(target, nums):
    sum = 0
    low, high = 0, 0
    res = float('inf')
    while(high<len(nums)):
        sum = sum + nums[high]
        while(sum>=target):
            length = high - low + 1
            res = min(res,length)
            sum = sum - nums[low]
            low += 1
        high += 1

    return res if res != float('inf') else 0

target1 = 7
nums1 = [2,3,1,2,4,3]

target2 = 4
nums2 = [1,4,4]

target3 = 11
nums3 = [1,1,1,1,1,1,1,1]

print(minSubArrayLen(target1, nums1))
print(minSubArrayLen(target2, nums2))
print(minSubArrayLen(target3, nums3))