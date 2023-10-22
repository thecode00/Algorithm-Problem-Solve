# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return 0

        # BST has bigger nodes on the right side than the current node
        self.bstToGst(root.right)
        self.total += root.val
        root.val = self.total
        # After add parent node and right side nodes to total than add left side nodes
        self.bstToGst(root.left)

        return root
