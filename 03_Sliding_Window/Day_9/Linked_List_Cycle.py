#https://leetcode.com/problems/linked-list-cycle/description/
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def createLinkedList(arr, pos):
    if not arr:
        return None

    nodes = [ListNode(x) for x in arr]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


def hasCycle(head):
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False


head1 = createLinkedList([3, 2, 0, -4],  1)
head2 = createLinkedList([1, 2], 0)
head3 = createLinkedList([1], -1)

print(hasCycle(head1))
print(hasCycle(head2))
print(hasCycle(head3))
