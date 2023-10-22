# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = cur = ListNode(0)
        while head:
            count = 1
            start = head.next
            # Count same node
            while start and start.val == head.val:
                count += 1
                start = start.next
            if count == 1:
                cur.next = head
                cur = cur.next
            # If not cur node when head = [1, 2, 2] we will return [1, 2, 2] so cut head.next
            head.next, head = None, start
        return root.next
