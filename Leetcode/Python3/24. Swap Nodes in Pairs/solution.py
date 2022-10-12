# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(0, head)
        while pre.next and pre.next.next:
            slow, fast = pre.next, pre.next.next
            pre.next, slow.next, fast.next = fast, fast.next, slow
            pre = slow
        return dummy.next
