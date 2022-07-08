# https://leetcode.com/problems/find-pivot-index/

# solution from here: https://leetcode.com/problems/find-pivot-index/discuss/109255/Short-Python-O(n)-time-O(1)-space-with-Explanation
class Solution:  # Runtime: 169 ms
    def pivotIndex(self, nums: List[int]) -> int:
        # If pivot index == 0 or -1 left_sum or right_sum will be 0
        left, right = 0, sum(nums)
        for idx, num in enumerate(nums):
            right -= num
            if left == right:
                return idx
            left += num
        return -1   # When there is no pivot index
