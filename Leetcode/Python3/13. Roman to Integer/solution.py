# https://leetcode.com/problems/roman-to-integer/

# Ref: https://leetcode.com/problems/roman-to-integer/discuss/264743/Clean-Python-beats-99.78.
class Solution:
    def romanToInt(self, s: str) -> int:
        roma_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            num += roma_dict[char]
        return num
