# https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:    # If end of depth return 0
                return 0

            left, right = dfs(node.left), dfs(node.right)
            if abs(left - right) > 1:
                self.result = False
                return 0    # Already found answer so can return any number
            else:
                return max(left, right) + 1
        dfs(root)
        return self.result
