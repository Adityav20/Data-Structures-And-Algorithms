#https://leetcode.com/problems/palindrome-linked-list/description/
"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
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
def isPalindrome(head):
    slow, fast = head, head

    if head is None:
        return True

    # Finding middle
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    # Skip middle node for odd length
    if fast != None:
        slow = slow.next

    # Reverse the second half
    prev = None
    curr = slow

    while curr != None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Compare both halves
    first = head
    second = prev

    while second != None:
        if first.val != second.val:
            return False

        first = first.next
        second = second.next

    return True


# Test cases
head1 = createLinkedList([1, 2, 2, 1])
head2 = createLinkedList([1, 2])
head3 = createLinkedList([1, 2, 3, 2, 1])
head4 = createLinkedList([1])

print(isPalindrome(head1))
print(isPalindrome(head2))
print(isPalindrome(head3))
print(isPalindrome(head4))
