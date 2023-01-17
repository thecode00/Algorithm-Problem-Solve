# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Ref: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solutions/35474/python-recursive-solution-with-detailed-comments-operate-linked-list-directly/?orderBy=most_votes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return

        if not head.next:
            return TreeNode(head.val)

        # slow = head
        # fast = slow.next.next
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(slow.val)
        temp = slow.next
        node = TreeNode(temp.val)
        slow.next = None
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(temp.next)

        return node

        