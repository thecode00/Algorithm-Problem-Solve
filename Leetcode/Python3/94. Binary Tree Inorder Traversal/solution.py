"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
Time Complexity: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Ref: https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/283746/All-DFS-traversals-(preorder-inorder-postorder)-in-Python-in-1-line
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []

        answer = inorder(root)
        return answer
