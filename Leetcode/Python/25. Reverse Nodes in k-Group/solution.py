# https://leetcode.com/problems/reverse-nodes-in-k-group/
# This problem is an extension of problem 92
# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = start = ListNode(0, head)
        count = 0
        while head:
            head = head.next
            count += 1
            if count == k:
                end = start.next
                for _ in range(k - 1):
                    next, end.next, start.next = start.next, end.next.next, end.next
                    start.next.next = next
                start = end
                count = 0
        return root.next
