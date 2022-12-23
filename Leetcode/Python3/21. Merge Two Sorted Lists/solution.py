# https://leetcode.com/problems/merge-two-sorted-lists/

# Ref: https://leetcode.com/problems/merge-two-sorted-lists/discuss/1826693/Python3-MERGING-Explained

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = ListNode()
        while list1 and list2:
            if list1.val >= list2.val:
                cur.next = list2
                list2, cur = list2.next, list2
            else:
                cur.next = list1
                list1, cur = list1.next, list1
        if list1 or list2:  # If there are remaining nodes, connect to cur node
            cur.next = list1 if list1 else list2
        return head.next    # Head is dummy node so return head.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Assign a list with a small value as list1
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
