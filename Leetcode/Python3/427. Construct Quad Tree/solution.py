# https://leetcode.com/problems/construct-quad-tree/


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def zip_node(x: int, y: int, length: int) -> Node:
            num = grid[y][x]
            node = Node(num, 1, None, None, None, None)
            if length == 1:
                print("1")
                return node
            for i in range(y, y + length):
                for j in range(x, x + length):
                    if grid[i][j] != num:
                        node.isLeaf = 0
                        node.topLeft = zip_node(x, y, length // 2)
                        node.topRight = zip_node(x + length // 2, y, length // 2)
                        node.bottomLeft = zip_node(x, y + length // 2, length // 2)
                        node.bottomRight = zip_node(x + length // 2, y + length // 2, length // 2)
                        return node

            return node   # All numbers are same
        return zip_node(0, 0, len(grid))
