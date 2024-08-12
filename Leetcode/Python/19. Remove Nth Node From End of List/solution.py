# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Ref: https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:    # When fast is None n = size so remove head
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


class Solution:  # O(N) But two pass
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        fast = head
        while fast.next and fast.next.next:
            length += 2
            fast = fast.next.next

        if fast.next:
            length += 1

        root = cur = ListNode(0, head)
        # Move to prev node fo remove node
        for _ in range(length - n):
            cur = cur.next
        cur.next = cur.next.next
        return root.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        root = prev = ListNode(-1, head)

        for _ in range(n):
            fast = fast.next

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next

        return root.next
