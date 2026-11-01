#https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1
"""
Given an array arr[] consisting of only 0's and 1's. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

Example 1:

Input: arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 0, 0, 1, 1, 1, 1, 1].

Example 2:

Input: arr[] = [1, 1]
Output: [1, 1]
Explanation: There are no 0s in the given array, so the modified array is [1, 1]
"""

def segregate0and1(arr):
    left = 0

    for right in range(len(arr)):
        if arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1

    return arr


arr1 = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]    
arr2 = [1,1]

print(segregate0and1(arr1))
print(segregate0and1(arr2))

#Time Complexity = O(n)
#Space Complexity = O(1)
