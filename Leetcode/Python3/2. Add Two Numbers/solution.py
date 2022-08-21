# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # Runtime: 95 ms
        head = cur = ListNode()
        prev = 0
        while l1 and l2:
            prev = l1.val + l2.val + (prev // 10)
            cur.next = ListNode(prev % 10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        # Check remain node
        while l1:
            prev = l1.val + (prev // 10)
            cur.next = ListNode(prev % 10)
            cur = cur.next
            l1 = l1.next
        while l2:
            prev = l2.val + (prev // 10)
            cur.next = ListNode(prev % 10)
            cur = cur.next
            l2 = l2.next
        # If prev >= 10 then add node 1
        if prev // 10:  
            cur.next = ListNode(1)
        return head.next
            
            