# https://leetcode.com/problems/delete-columns-to-make-sorted/


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = 0
        for x in range(len(strs[0])):
            for y in range(1, len(strs)):
                if strs[y-1][x] > strs[y][x]:
                    delete += 1
                    break
        return delete
