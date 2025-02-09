# https://leetcode.com/problems/count-number-of-bad-pairs/description

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        pair_count = defaultdict(int)
        bad_pairs = 0

        for idx in range(len(nums)):
            # (j - i != nums[j] - nums[i]) can be (nums[i] - i != nums[j] - j)
            pair_number = nums[idx] - idx
            bad_pairs += idx - pair_count[pair_number]

            pair_count[pair_number] += 1

        return bad_pairs
