# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # print(int(a, 2), int(b, 2))   Port binary to devimal
        a, b = int(a, 2), int(b, 2)
        # Bin() return 0b10101... so use slice [2:] to cut 0b
        return str(bin(a + b))[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        b = b.zfill(len(a))
        result = []
        carry = 0
        for idx in range(len(a) - 1, -1, -1):
            Q1 = int(a[idx]) ^ int(b[idx])
            Q2 = int(a[idx]) & int(b[idx])
            Q3 = Q1 & carry
            result.append(str(Q1 ^ carry))
            carry = Q2 | Q3
        if carry:
            result.append("1")
        return "".join(result[::-1])
