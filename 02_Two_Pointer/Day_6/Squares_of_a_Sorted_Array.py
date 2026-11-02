#https://leetcode.com/problems/squares-of-a-sorted-array/description/
"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

def sortedSquares(nums):
    n = len(nums)
    start, end = 0, n-1
    ans = [0]*n
    for i in range(n-1,-1,-1):
        if abs(nums[start]) >= abs(nums[end]):
            ans[i] = nums[start] * nums[start]
            start+=1
        else:
            ans[i] = nums[end] * nums[end]
            end-=1

    return ans

nums1 = [-4,-1,0,3,10]
nums2 = [-7,-3,2,3,11]

print(sortedSquares(nums1))
print(sortedSquares(nums2))

#Time Complexity = O(n)
#Space Complexity = O(n)