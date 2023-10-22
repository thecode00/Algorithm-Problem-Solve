# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:  # Runtime: 95 ms
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


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode(0)
        carry = 0  # If l1.val + l2.val >= 10 carry will 1 else 0
        while l1 or l2 or carry:
            total = 0
            # length of l1, l2 is different so check l1, l2 is None
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            q, r = divmod(total + carry, 10)
            carry = 1 if q else 0
            cur.next = ListNode(r)
            cur = cur.next
        return head.next  # head node is dummy value return head.next
