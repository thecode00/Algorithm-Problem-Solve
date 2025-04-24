# https://leetcode.com/problems/count-largest-group/description

class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sum_hash = defaultdict(int)
        largest_group = 0

        for num in range(1, n + 1):
            digit_sum = self.getDigitSum(num)

            digit_sum_hash[digit_sum] += 1
            largest_group = max(largest_group, digit_sum_hash[digit_sum])
        
        group_count = 0
        # Find largest group size
        for count in digit_sum_hash.values():
            if count == largest_group:
                group_count += 1

        return group_count
        
    def getDigitSum(self, n: int) -> int:
        total = 0

        while n > 0:
            q, r = divmod(n, 10)

            total += r
            n = q
        
        return total