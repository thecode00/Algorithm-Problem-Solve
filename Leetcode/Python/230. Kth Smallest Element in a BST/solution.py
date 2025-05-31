# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]

        while root.left:
            stack.append(root.left)
            root = root.left

        order = 1

        while order < k:
            order += 1

            cur = stack.pop().right

            while cur:
                stack.append(cur)
                cur = cur.left

        return stack.pop().val
