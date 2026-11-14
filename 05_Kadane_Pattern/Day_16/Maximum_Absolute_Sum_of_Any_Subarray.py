#https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
"""
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:
If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
 
Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
"""
def maxAbsoluteSum(nums):
    maxending = nums[0]
    minending = nums[0]
    ans = abs(nums[0])
    for i in range(1, len(nums)):
        v1 = maxending + nums[i]
        v2 = nums[i]
        v3 = minending + nums[i]
        maxending = max(v1, v2, v3)
        minending = min(v1, v2, v3)
        ans = max(abs(maxending), ans, abs(minending))
    return ans

nums1 = [1,-3,2,3,-4]
nums2 = [2,-5,1,-4,3,-2]

print(maxAbsoluteSum(nums1))
print(maxAbsoluteSum(nums2))

#Time Complexity = O(n)
#Space Complexity = O(1)