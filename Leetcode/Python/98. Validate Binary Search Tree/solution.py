# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev, bst_list = None, []

        # Inorder
        while root or bst_list:
            while root:
                bst_list.append(root)
                root = root.left
            root = bst_list.pop()

            if prev is not None and prev >= root.val:
                return False

            prev = root.val
            root = root.right

        return True


class Solution:  # Recursive
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.search(root, None, None)

    def search(self, root: Optional[TreeNode], min_value: int, max_value: int) -> bool:
        if not root:
            return True

        if (min_value is not None and root.val <= min_value) or (max_value is not None and max_value <= root.val):

            return False

        return self.search(root.left, min_value, root.val) and self.search(root.right, root.val, max_value)
