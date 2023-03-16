# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        node = TreeNode(postorder.pop())
        # Find center index
        index = inorder.index(node.val)
        # Split left and right by index
        node.right = self.buildTree(inorder[index+1:], postorder)
        node.left = self.buildTree(inorder[:index], postorder)
        return node
    

# Better solution: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solutions/221681/a-better-python-solution/?orderBy=most_votes
