#https://leetcode.com/problems/maximum-product-subarray/description/
"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
def maxProduct(nums):
    maxending = nums[0]
    minending = nums[0] #For [-2,3,-4]
    ans = nums[0]
    for i in range(1, len(nums)):
        v1 = maxending * nums[i]
        v2 = nums[i]
        v3 = minending * nums[i]
        maxending = max(v1, v2, v3)
        minending = min(v1, v2, v3)
        ans = max(maxending, ans, minending)
    return ans

nums1 = [2,3,-2,4]
nums2 = [-2,0,-1]
nums3 = [-2,3,-4]

print(maxProduct(nums1))
print(maxProduct(nums2))
print(maxProduct(nums3))

#Time Complexity = O(n)
#Space Complexity = O(1)