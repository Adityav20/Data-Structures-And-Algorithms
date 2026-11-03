#https://leetcode.com/problems/3sum-closest/description/
"""
You are given an integer array nums of length n and an integer target.

Find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

def threeSumClosest(nums, target):
    nums.sort()
    result = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(target - total) < abs(target - result):
                result = total

            if total == target:
                return target
            elif total < target:
                left += 1
            else:
                right -= 1

    return result

nums1 = [-1,2,1,-4] 
target1 = 1

nums2 = [0,0,0]
target2 = 1

print(threeSumClosest(nums1,target1))
print(threeSumClosest(nums2,target2))

#Time complexity: O(n^2)
#Space complexity: O(1)