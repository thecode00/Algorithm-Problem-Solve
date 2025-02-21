# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.value_set = set()
        self.dfs(root)

    def find(self, target: int) -> bool:
        return target in self.value_set

    def dfs(self, root):
        if not root:
            return

        stack = [root]
        root.val = 0

        while stack:
            cur = stack.pop()
            self.value_set.add(cur.val)

            if cur.left:
                cur.left.val = cur.val * 2 + 1
                stack.append(cur.left)

            if cur.right:
                cur.right.val = cur.val * 2 + 2
                stack.append(cur.right)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
