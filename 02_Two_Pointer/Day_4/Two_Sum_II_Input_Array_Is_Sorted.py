#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""
You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.
Find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers index1 and index2 as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
"""

def twoSum(numbers: list[int], target: int) -> list[int]:
    i = 0
    j = len(numbers)-1
    while i<j:
        sum = numbers[i] + numbers[j]
        if sum==target:
            return [i+1,j+1]
        if sum>target:
            j-=1
        if sum<target:
            i+=1
    return None

arr1 = [2,7,11,15]
arr2 = [2,3,4]

print(twoSum(arr1,9))
print(twoSum(arr2,6))

#Time Complexity = O(n)
#Space Complexity = O(1)

"""
This algo will only work when the array is sorted.
But when the array is not sorted than we will apply different algo

Why?
Because manually sorting the array will change the index.

If question asked to give the int rather than the position(index),
then above solution can also be applied
"""