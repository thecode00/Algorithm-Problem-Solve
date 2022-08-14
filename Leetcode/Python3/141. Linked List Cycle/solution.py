# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# TODO: optimization
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:   # Runtime: 109 ms
        if head == None or head.next == None:
            return False
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False