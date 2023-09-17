# https://leetcode.com/problems/binary-search-tree-iterator/
# Ref: https://leetcode.com/problems/binary-search-tree-iterator/solutions/52647/nice-comparison-and-short-solution/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []

    def next(self) -> int:
        # Add nodes in in-order traversal order.
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left

        cur = self.stack.pop()
        self.root = cur.right
        return cur.val

    def hasNext(self) -> bool:
        return self.root != None or self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
