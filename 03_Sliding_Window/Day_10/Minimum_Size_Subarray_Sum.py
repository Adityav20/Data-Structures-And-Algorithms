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

def minSubArrayLen(arr, k):
    sum = 0
    low,high,length = 0, 0, 0
    res = float('inf')
    while high<len(arr):
        sum = sum + arr[high]
        while sum>=k:
            length = high-low+1
            res = min(res,length)
            sum = sum - arr[low]
            low+=1
        high+=1
            
    return res if res != float('inf') else 0


arr1 = [2,3,1,2,4,3]
target1 = 7

arr2 = [1,4,4]
target2 = 4

arr3 = [1,1,1,1,1,1,1,1]
target3 = 11

print(minSubArrayLen(arr1,target1))
print(minSubArrayLen(arr2,target2))
print(minSubArrayLen(arr3,target3))

#Time Complexity = O(n)
#Space Complexity = O(1)