# https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        for char in columnTitle:
            number *= 26
            number += ord(char) - ord("A") + 1

        return number
