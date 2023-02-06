# https://leetcode.com/problems/shuffle-the-array/


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        x, y = 0, len(nums) // 2
        while x < len(nums) // 2:
            result.append(nums[x])
            result.append(nums[y])
            x += 1
            y += 1
        return result
