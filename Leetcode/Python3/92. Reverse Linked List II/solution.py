# https://leetcode.com/problems/reverse-linked-list-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = start = ListNode(0, head)
        for _ in range(left - 1):  # Set start index left - 1
            start = start.next
        end = start.next  # End node of reverse linked list
        for _ in range(right - left):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp
        return root
