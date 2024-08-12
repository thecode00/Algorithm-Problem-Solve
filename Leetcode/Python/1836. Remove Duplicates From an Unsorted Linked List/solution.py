# https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        exist = set()
        cur = head
        # The first element is always unique, so there is no need to check if prev is null
        prev = None

        while cur:
            if cur.val in exist:
                prev.next = cur.next
            exist.add(cur.val)
            prev = cur
            cur = cur.next
        return head
