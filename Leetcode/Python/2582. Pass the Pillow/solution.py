# https://leetcode.com/problems/pass-the-pillow/description

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # n - 1 = one cycle edge to edge
        idx = time % (n - 1)
        to_right = True if (time // (n - 1)) % 2 == 0 else False

        if to_right:
            return 1 + idx
        else:
            return n - idx
