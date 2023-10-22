# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy =  prev = ListNode(None, head)
        while prev.next and prev.next.next:
            first, second = prev.next, prev.next.next
            prev.next = second
            first.next, second.next = second.next, first
            prev = first
        return dummy.next

