#https://leetcode.com/problems/4sum/description/
"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

def threeSum(nums, target):
    s = set()
    nums.sort()
    for i in range(len(nums)-2):
        j = i+1
        k = len(nums)-1
        while j<k:
            sum = nums[i] + nums [j] + nums[k]
            if sum == target:
                s.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif sum < target:
                j+=1
            else:
                k-=1

    ans = list(s)
    return ans

def fourSum(nums, target):
    s = set()
    nums.sort()
    for i in range(len(nums) - 3):
        remaining_target = target - nums[i]

        triplets = threeSum(nums[i + 1:], remaining_target)

        for triplet in triplets:
            s.add((nums[i],) + triplet)

    return [list(q) for q in sorted(s)]

nums1 = [1,0,-1,0,-2,2], target1 = 0
nums2 = [2,2,2,2,2], target2 = 8

