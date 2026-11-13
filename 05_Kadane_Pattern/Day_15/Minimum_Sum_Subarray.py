#https://www.geeksforgeeks.org/problems/smallest-sum-contiguous-subarray/1
"""
Given an array arr[], find the minimum sum of a subarray containing atleast one element in the given array.

Example 1:
Input: arr = [3, -4, 2, -3, -1, 7, -5]
Output: -6
Explanation: The subarray [-4, 2, -3, -1] has the minimum sum, which is -6.

Example 2:
Input: arr = [4, -6, 3, -2, 5, -8, 2]
Output: -8
Explanation: The subarray [-8] has the minimum sum, which is -8.

Example 3:
Input: arr = [2, 6, 8, 1, 4]
Output: 1
Explanation: The subarray [1] has the minimum sum, which is 1.
"""
def minSubarraySum(nums):
    bestending = nums[0]
    ans = nums[0]
    for i in range(1, len(nums)):
        v1 = bestending + nums[i]
        v2 = nums[i]
        bestending = min(v1,v2)
        ans = min(ans, bestending)
    return ans

arr1 = [3, -4, 2, -3, -1, 7, -5]
arr2 = [4, -6, 3, -2, 5, -8, 2]
arr3 = [2, 6, 8, 1, 4]

print(minSubarraySum(arr1))
print(minSubarraySum(arr2))
print(minSubarraySum(arr3))

#Time Complexity = O(n)
#Space Complexity = O(1)