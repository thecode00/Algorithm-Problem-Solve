# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre = head, None
        while cur:
            next, cur.next = cur.next, pre
            pre, cur = cur, next
            # Same code: cur.next, pre, cur = pre, cur, cur.next
        return pre
