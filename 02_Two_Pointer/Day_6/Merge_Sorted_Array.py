#https://leetcode.com/problems/merge-sorted-array/description/
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n. 

Example 1:

Input: nums1 = [1,2,3,7], nums2 = [2,5,6]
Output: [1,2,2,3,5,6,7]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], nums2 = []
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
"""

def merge(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    i,j,k = 0,0,0
    ans = [0] * (m+n)
    while i<m and j<n:
        if nums1[i]<=nums2[j]:
            ans[k] = nums1[i]
            i+=1
            k+=1
        else:
            ans[k] = nums2[j]
            j+=1
            k+=1

    while i<m: #Case where nums1 is longer
        ans[k] = nums1[i]
        i+=1
        k+=1

    while j<n: ##Case where nums2 is longer
        ans[k] = nums2[j]
        j+=1
        k+=1

    return ans

nums1a = [1,2,3,7]
nums2a = [2,5,6]

nums1b = [1]
nums2b = []

print(merge(nums1a,nums2a))
print(merge(nums1b,nums2b))