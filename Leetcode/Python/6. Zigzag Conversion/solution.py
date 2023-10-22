# https://leetcode.com/problems/zigzag-conversion/
# Ref: https://leetcode.com/problems/zigzag-conversion/solutions/3404/python-o-n-solution-in-96ms-99-43/?orderBy=most_votes

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        result = ["" for _ in range(numRows)]
        index = 0
        step = 1
        for char in s:
            result[index] += char

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step
        return "".join(result)
