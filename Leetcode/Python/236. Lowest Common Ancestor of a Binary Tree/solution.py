# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  # First try, to many subtree search
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q)

    def helper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        is_p_left = self.cover(root.left, p)
        is_q_left = self.cover(root.left, q)
        # p, q not in same subtree current root is ancestor
        if is_p_left != is_q_left:
            return root

        if is_p_left:
            return self.helper(root.left, p, q)
        else:
            return self.helper(root.right, p, q)

    def cover(self, root: Optional[TreeNode], target: TreeNode) -> bool:
        if not root:
            return False

        if root == target:
            return True

        return self.cover(root.left, target) or self.cover(root.right, target)


class Solution:  # Second try
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (not root) or (root is p) or (root is q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # when p not in q's subtree, p and q split left and right root is LCA
        if left and right:
            return root
        # p in q's subtree
        return left if left else right
