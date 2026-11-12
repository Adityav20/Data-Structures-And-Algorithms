#https://leetcode.com/problems/middle-of-the-linked-list/description/
"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""
# Each node contains a value and a reference to the next node
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

# Converts input array into a linked list
def createLinkedList(arr):
    if not arr:
        return None

    nodes = [ListNode(x) for x in arr]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    return nodes[0]

# Main Solution
def middleNode(head):
    slow, fast = head, head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow

# Convert linked list into a Python list for printing
def linkedListToList(head):
    result = []

    while head != None:
        result.append(head.val)
        head = head.next

    return result

# Test cases
head1 = createLinkedList([1, 2, 3, 4, 5])
head2 = createLinkedList([1, 2, 3, 4, 5, 6])

print(linkedListToList(middleNode(head1)))
print(linkedListToList(middleNode(head2)))

#Time Complexity = O(n)
#Space Complexity = O(1)