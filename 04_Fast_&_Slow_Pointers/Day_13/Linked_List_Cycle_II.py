#https://leetcode.com/problems/linked-list-cycle-ii/description/
"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
"""
#Each node contains a value (val) and a reference to the next node (next)
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

#Converts input array into a real linked list
def createLinkedList(arr, pos):
    if not arr:
        return None

    nodes = [ListNode(x) for x in arr]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


# Main Solution
def detectCycle(head):
    slow, fast = head, head
    count = 0
    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
                count += 1
            return f'tail connects to node index {count}'
    return 'There is no cycle in the linked list.'

# Test cases
head1 = createLinkedList([3, 2, 0, -4], 1)
head2 = createLinkedList([1, 2], 0)
head3 = createLinkedList([1], -1)

print(detectCycle(head1))
print(detectCycle(head2))
print(detectCycle(head3))