# https://leetcode.com/problems/range-sum-of-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  # Bruteforce
    total = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def find_value(root):
            if not root:
                return

            if low <= root.val <= high:
                self.total += root.val

            find_value(root.left)
            find_value(root.right)

        find_value(root)
        return self.total


class Solution:  # DFS recursion
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            else:
                return dfs(node.left) + dfs(node.right) + node.val
        return dfs(root)


class Solution:  # DFS iteration
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        total = 0
        while stack:
            node = stack.pop()
            if node:
                if node.val < low:
                    stack.append(node.right)
                elif node.val > high:
                    stack.append(node.left)
                else:
                    total += node.val
        return total
