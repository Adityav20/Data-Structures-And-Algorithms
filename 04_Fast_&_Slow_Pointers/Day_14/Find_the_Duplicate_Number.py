#https://leetcode.com/problems/find-the-duplicate-number/description/
"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
"""
def findDuplicate(nums):
    slow, fast = 0, 0
    for i in range(len(nums)):
        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]
        while slow == fast:
            slow = 0
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
            return slow


nums1 = [1,3,4,2,2]
nums2 = [3,1,3,4,2]
nums3 = [3,3,3,3,3]

print(findDuplicate(nums1))
print(findDuplicate(nums2))
print(findDuplicate(nums3))

#Time Complexity = O(n)
#Space Complexity = O(1)