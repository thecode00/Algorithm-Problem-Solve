"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
Time Complexity: O(N)
Ref: https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/283746/All-inorder-traversals-(preorder-inorder-postorder)-in-Python-in-1-line
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def inorder(node: TreeNode) -> None:
            if not node:
                return

            inorder(node.left)
            answer.append(node.val)
            inorder(node.right)

        inorder(root)
        return answer


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []

        answer = inorder(root)
        return answer
