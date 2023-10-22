# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None

        right_side_view = []
        # queue contains the nodes of the tree at each level.
        queue = deque([root])
        while queue:
            # Add right side view node value
            right_side_view.append(queue[-1].val)

            length = len(queue)
            for _ in range(length):
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

        return right_side_view
