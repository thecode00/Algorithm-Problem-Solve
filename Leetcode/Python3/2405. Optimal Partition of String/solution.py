# https://leetcode.com/problems/optimal-partition-of-string/description/


class Solution:
    def partitionString(self, s: str) -> int:
        used = set()
        count = 0
        for char in s:
            if char in used:
                count += 1
                used.clear()
            used.add(char)
            
        return count + 1 if used else count

