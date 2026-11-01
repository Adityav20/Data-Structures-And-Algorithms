#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
"""
Given the head of a sorted array, delete all duplicates such that each element appears only once. Return the array sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

def deleteDuplicates(head):
    i = 0
    j = 1

    while j<len(head):
        if head[j]==head[j-1]:
            j+=1
            continue
        head[i+1] = head[j]
        i+=1
        j+=1

    del head[i+1:] #For reducing space complexity
    return head[:i+1] #returning only till duplicate value



head1 = [1,1,2]
head2 = [1,1,2,3,3]

print(deleteDuplicates(head1))
print(deleteDuplicates(head2))

#Time Complexity = O(n)
#Space Complexity = O(1)