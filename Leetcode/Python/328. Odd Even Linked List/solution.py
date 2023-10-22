# https://leetcode.com/problems/odd-even-linked-list/

# Ref: https://leetcode.com/problems/odd-even-linked-list/discuss/133345/With-detailed-explanation-or-Python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:    # Avoid blank list
            return head
        odd = head
        even = head.next
        even_head = even    # Save even index head node
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head    # Link odd_index linked list to even_index linked list head
        return head
