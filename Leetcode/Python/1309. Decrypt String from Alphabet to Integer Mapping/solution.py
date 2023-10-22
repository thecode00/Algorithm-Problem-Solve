# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

# refer: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/discuss/470770/Python-3-(two-lines)-(beats-100)-(16-ms)-(With-Explanation)
class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26, 0, -1):
            # If i > 9: "#" * True(1) when i < 10: "#" * False(0)
            s = s.replace(str(i) + "#" * (i > 9), chr(96 + i))
        return s


