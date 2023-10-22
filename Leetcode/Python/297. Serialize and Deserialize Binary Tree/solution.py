# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        answer = []
        while queue:
            node = queue.popleft()
            if node:
                answer.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                answer.append("#")

        print("".join(answer))
        return " ".join(answer)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "#":  # If root is None serialize() return "#"
            return None
        nodes = data.split()

        root = TreeNode(nodes[0])
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if nodes[index] != "#":
                node.left = TreeNode(nodes[index])
                queue.append(node.left)
            index += 1

            if nodes[index] != "#":
                node.right = TreeNode(nodes[index])
                queue.append(node.right)
            index += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
