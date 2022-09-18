# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # print(int(a, 2), int(b, 2))   Port binary to devimal
        a, b = int(a, 2), int(b, 2)
        return str(bin(a + b))[2:]  # Bin() return 0b10101... so use slice [2:] to cut 0b
