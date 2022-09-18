# https://leetcode.com/problems/array-partition/


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the small ones to group them as small as possible.
        nums.sort()
        answer = 0
        for idx in range(0, len(nums), 2):
            answer += nums[idx]
        return answer

    # Ref: https://leetcode.com/problems/array-partition/discuss/102161/Python-1-line-(sorting-is-accepted)
    def arrayPairSum(self, nums):  # One line solution
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
