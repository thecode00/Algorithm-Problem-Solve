# https://leetcode.com/problems/rotate-list/
# This problem is extension of problem 19
# Problem 19: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        root = ListNode(0, head)
        # Measure list size
        fast = head
        length = 1
        while fast.next and fast.next.next:
            length += 2
            fast = fast.next.next
        if fast.next:
            length += 1
        # Remove not necessary rotate
        k %= length
        if k == 0:
            return root.next

        slow = fast = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next, root.next, fast.next = None, slow.next, root.next
        return root.next
