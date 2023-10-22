# https://leetcode.com/problems/insertion-sort-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  # My first answer
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        def insert(node):
            if not dummy.next:
                dummy.next = node
                return

            prev, cur = dummy, dummy.next
            while cur:
                if cur.val > node.val:
                    prev.next = node
                    node.next = cur
                    return
                prev, cur = cur, cur.next

            prev.next = node
            node.next = None
        pre = None
        n = head
        while n:
            pre = n
            n = n.next
            pre.next = None
            insert(pre)
        return dummy.next


class Solution:  # Second answer
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next
            cur = dummy
        return dummy.next


class Solution:  # Third answer
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next
            if head and cur.val > head.val:
                cur = dummy
        return dummy.next
