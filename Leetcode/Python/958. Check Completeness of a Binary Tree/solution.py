# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# Ref: https://leetcode.com/problems/check-completeness-of-a-binary-tree/solutions/205682/java-c-python-bfs-solution-and-dfs-soluiton/?orderBy=most_votes


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        idx = 0
        serialize = [root]
        while serialize[idx]:
            serialize.append(serialize[idx].left)
            serialize.append(serialize[idx].right)
            idx += 1
        # Non-null nodes should not exist after the current null node because all child nodes of the previous level have been added previously
        if any(serialize[idx:]):
            return False
        return True
