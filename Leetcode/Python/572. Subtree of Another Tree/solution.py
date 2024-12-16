# https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.subTree(root, subRoot)

    def subTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        # If the current node's value matches the subRoot's root value,
        # check if the two subtrees are exactly the same
        elif root.val == subRoot.val and self.checkSameTree(root, subRoot):
            return True
        # If not found at the current node, continue searching in the left and right subtrees.
        return self.subTree(root.left, subRoot) or self.subTree(root.right, subRoot)

    def checkSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if (not root or not subRoot) or (root.val != subRoot.val):
            return False

        return self.checkSameTree(root.left, subRoot.left) and self.checkSameTree(root.right, subRoot.right)
