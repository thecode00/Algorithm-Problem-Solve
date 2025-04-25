# https://leetcode.com/problems/count-of-interesting-subarrays/description

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1  # Initial prefix % modulo is 0

        for num in nums:
            if num % modulo == k:
                prefix += 1

            # cnt % MOD = k, prefix[j] - prefix[i - 1] = cnt
            # (prefix[j] - prefix[i - 1]) % MOD = k -> prefix[i - 1] = (prefix[j] - k) % MOD
            target = (prefix - k) % modulo
            count += freq[target]

            freq[prefix % modulo] += 1

        return count