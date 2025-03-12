# https://leetcode.com/problems/path-sum-iii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.search(root, targetSum, defaultdict(int), 0)

    def search(self, root: Optional[TreeNode], targetSum: int, pathSumHash: Dict[int, int], totalSum: int):
        if not root:
            return 0

        totalSum += root.val
        key = totalSum - targetSum
        pathCount = pathSumHash[key]

        if totalSum == targetSum:
            pathCount += 1

        self.savePathHash(pathSumHash, totalSum, 1)
        pathCount += self.search(root.left, targetSum, pathSumHash, totalSum)
        pathCount += self.search(root.right, targetSum, pathSumHash, totalSum)
        self.savePathHash(pathSumHash, totalSum, -1)

        return pathCount

    def savePathHash(self, pathSumHash: Dict[int, int], key: int, diff: int):
        pathSumHash[key] += diff
        if pathSumHash[key] == 0:
            del pathSumHash[key]
