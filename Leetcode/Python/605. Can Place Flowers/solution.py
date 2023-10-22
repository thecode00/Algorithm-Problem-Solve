# https://leetcode.com/problems/can-place-flowers/

"""
Time complexity: O(N)
Space complexity: O(1)
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n > sum(divmod(len(flowerbed), 2)):
            return False
        if n == 0:
            return True
        for idx, flower in enumerate(flowerbed):
            # If idx == 0 cant search idx - 1 and if idx == len(flowerbed) - 1 index is last of flowerbed so cant search idx + 1
            if not flower and (
                    idx == 0 or not flowerbed[idx - 1]) and (
                    idx == len(flowerbed) - 1 or not flowerbed[idx + 1]):
                n -= 1
                if n == 0:  # All flowers planted
                    return True
                flowerbed[idx] = 1  # Plant current bed
        return False
