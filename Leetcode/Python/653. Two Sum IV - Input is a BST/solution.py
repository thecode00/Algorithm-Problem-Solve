# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def getBSTNodes(root: Optional[TreeNode]):
            if not root:
                return
            # When traversing a BST with an in-order traversal, the nodes are visited in ascending order.
            getBSTNodes(root.left)
            node_list.append(root.val)
            getBSTNodes(root.right)

        node_list = []
        getBSTNodes(root)

        number_hash = set()

        for num in node_list:
            if k - num in number_hash:
                return True
            number_hash.add(num)

        return False


class Solution:  # Leetcode bug
    node_list = []

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.getBSTNodes(root)

        number_hash = set()

        for num in self.node_list:
            if k - num in number_hash:
                return True
            number_hash.add(num)

        return False

    def getBSTNodes(self, root: Optional[TreeNode]):
        if not root:
            return

        # When traversing a BST with an in-order traversal, the nodes are visited in ascending order.
        self.getBSTNodes(root.left)
        self.node_list.append(root.val)
        self.getBSTNodes(root.right)
