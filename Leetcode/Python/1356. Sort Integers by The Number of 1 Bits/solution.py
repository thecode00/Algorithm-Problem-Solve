# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_bits(num: int) -> int:
            count = 0
            while num > 0:
                count += num & 1
                num >>= 1
            return count
        # Sort 1bits count, ascending number
        arr.sort(key=lambda x: (count_bits(x), x))
        return arr
