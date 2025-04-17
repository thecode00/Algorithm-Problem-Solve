# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        hash = dict()

        for idx, num in enumerate(nums):
            if num not in hash:
                hash[num] = []
            else:
                for i in hash[num]:
                    if (i * idx) % k == 0:
                        pairs += 1
            
            hash[num].append(idx)

        return pairs
