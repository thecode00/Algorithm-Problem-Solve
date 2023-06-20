# https://leetcode.com/problems/sort-list/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        half = None
        slow = fast = head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None    # Cut half listnode

        # Split nodes to single node.
        left, right = self.sortList(head), self.sortList(slow)
        return self.mergeSort(left, right)

    def mergeSort(self, left: ListNode, right: ListNode) -> ListNode:
        if left and right:
            if left.val > right.val:
                left, right = right, left
            left.next = self.mergeSort(left.next, right)
        return left or right    # Same code: return left if left else right


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        nums.sort()
        dummy = node = ListNode(0)
        for num in nums:
            node.next = ListNode(num)
            node = node.next
        return dummy.next
