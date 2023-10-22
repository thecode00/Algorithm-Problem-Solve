# https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(map(str, digits)))
        return list(map(int, str(number + 1)))
