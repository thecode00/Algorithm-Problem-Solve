# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description

class Solution:  # Second try, divide and conquer
    def findKthBit(self, n: int, k: int) -> str:
        if n <= 1:
            return "0"

        length = (1 << n) - 1
        # k is 1-index so add 1
        half = (length // 2) + 1

        # k in left half
        if k < half:
            return self.findKthBit(n - 1, k)
        elif k == half:
            return "1"
        else:  # k in right half
            target = self.findKthBit(n - 1, length - k + 1)
            if target == "1":
                return "0"
            else:
                return "1"


class Solution:  # First try, no algorithm just implement
    def findKthBit(self, n: int, k: int) -> str:
        bits = ["0"]

        while n > 1:
            size = len(bits)
            bits.append("1")

            for idx in range(size - 1, -1, -1):
                if bits[idx] == "1":
                    bits.append("0")
                else:
                    bits.append("1")

            n -= 1

        return bits[k - 1]
