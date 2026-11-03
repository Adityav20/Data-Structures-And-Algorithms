#https://www.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x5549/1
"""
Given an array arr[] of distinct integers and an integer sum, count the number of unique triplets of elements whose sum is strictly less than sum. A triplet is identified only by the three elements it contains, so different permutations of the same three elements are counted as one triplet.

Example 1:

Input: sum = 2, arr[] = [-2, 0, 1, 3]
Output:  2
Explanation: Triplets with sum less than 2 are (-2, 0, 1) and (-2, 0, 3). 

Example 2:

Input: sum = 12, arr[] = [5, 1, 3, 4, 7]
Output: 4
Explanation: Triplets with sum less than 12 are (1, 3, 4), (5, 1, 3), (1, 3, 7) and (5, 1, 4).
"""

def countTriplets(sum, arr):
    arr.sort()
    ans = 0
    closest_sum = arr[0] + arr[1] + arr[2]
    n = len(arr)
    for i in range(n-2):
        left, right = i+1, n-1
        while(left<right):
            s = arr[i] + arr[left] + arr[right]
            if abs(s - sum) < abs(closest_sum - sum):
                closest_sum = s
            if s >= sum:
                right = right-1
            else:
                ans = ans + (right-left)
                left = left+1
    return ans

nums1 = [-2, 0, 1, 3] 
sum1 = 2

nums2 = [5, 1, 3, 4, 7]
sum2 = 12

print(countTriplets(sum1, nums1))
print(countTriplets(sum2, nums2))

