#https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
"""
Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Example 1:
Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.

Example 2:
Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.

Example 3:
Input: arr[] = [100, 200, 300, 400], k = 1
Output: 400
Explanation: arr3 = 400, which is maximum.
"""

def maxSubarraySum(arr, k):
    sum = 0
    low,high = 0, k-1
    res = 0
    for i in range(k):
        sum = sum + arr[i]
    while k < len(arr):
        res = max(res,sum)
        low+=1
        high+=1
        if high==len(arr):
            break
        sum = sum - arr[low - 1]
        sum = sum + arr[high]

    return res

arr1 = [100, 200, 300, 400]
k1 = 2

arr2 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k2 = 4

arr3 = [100, 200, 300, 400]
k3 = 1

print(maxSubarraySum(arr1,k1))
print(maxSubarraySum(arr2,k2))
print(maxSubarraySum(arr3,k3))

#Time Complexity = O(n)
#Space Complexity = O(1)