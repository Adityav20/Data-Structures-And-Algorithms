#https://leetcode.com/problems/maximum-sum-circular-subarray/description/
"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
"""
def maxSubarraySumCircular(nums):
    bestending = nums[0]
    minending = nums[0]
    ans = nums[0]
    minans = nums[0]
    total = nums[0]

    for i in range(1, len(nums)):
        v1 = bestending + nums[i]
        v2 = nums[i]
        v3 = minending + nums[i]

        # Maximum subarray sum
        bestending = max(nums[i], bestending + nums[i])
        ans = max(ans, bestending)

        # Minimum subarray sum
        minending = min(nums[i], minending + nums[i])
        minans = min(minans, minending)

        total += nums[i]
        
    # All negative numbers
    if ans < 0:
        return ans

    return max(ans, total - minans)

nums1 = [1,-2,3,-2]
nums2 = [5,-3,5]
nums3 = [-3,-2,-3]
nums4 = [3,-1,2,-1]
nums5 = [-2,2,-2,9]


print(maxSubarraySumCircular(nums1))
print(maxSubarraySumCircular(nums2))
print(maxSubarraySumCircular(nums3))
print(maxSubarraySumCircular(nums4))
print(maxSubarraySumCircular(nums5))

#Time Complexity = O(n)
#Space Complexity = O(1)