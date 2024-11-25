# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  # Recursion
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.searchDepth(root, 1)

    def searchDepth(self, root: Optional[TreeNode], cur_depth: int) -> int:
        if not root:
            return float("inf")

        # Leaf node
        if not root.left and not root.right:
            return cur_depth

        left_depth, right_depth = self.searchDepth(
            root.left, cur_depth + 1), self.searchDepth(root.right, cur_depth + 1)

        return min(left_depth, right_depth)


class Solution:  # Iteration
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 1
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                # Leat node
                if not node.left and not node.right:
                    return depth

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return -1   # Detect error
