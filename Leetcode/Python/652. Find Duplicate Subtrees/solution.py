# https://leetcode.com/problems/find-duplicate-subtrees/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        node_hash = defaultdict(list)

        def search(node: Optional[TreeNode]) -> str:
            if not node:
                return "None"
            if node:
                # Inorder serialize make error: https://leetcode.com/problems/find-duplicate-subtrees/discuss/106011/Java-Concise-Postorder-Traversal-Solution/108467
                subtree = "/".join([search(node.left), search(node.right), str(node.val)])
                # print(subtree)
                node_hash[subtree].append(node)
                return subtree

        search(root)
        print(node_hash)
        return [value[0] for value in node_hash.values() if value[1:]]
