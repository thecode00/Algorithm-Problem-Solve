# https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    If declare answer variable in the diameterOfBinaryTree function,
    Error occur when assigning value to answer variable in dfs function
    """
    answer = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)
            self.answer = max(left + right, self.answer)    # Compare each node diameter with answer
            return max(left, right) + 1
        dfs(root)
        return self.answer
