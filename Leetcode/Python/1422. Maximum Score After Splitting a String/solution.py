# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description

class Solution:
    def maxScore(self, s: str) -> int:
        one = 0

        for num in s:
            one += int(num)

        zero = 0
        max_score = 0

        for idx in range(len(s) - 1):
            if int(s[idx]) == 0:
                zero += 1
            else:
                one -= 1

            max_score = max(max_score, zero + one)

        return max_score


class Solution:
    def maxScore(self, s: str) -> int:
        zero = one = 0
        max_score = -float("inf")
        # score = left_zero + right_one = left_zero + total_one - left_one
        # We need maximize left_zero - left_one
        for idx in range(len(s) - 1):
            if s[idx] == "1":
                one += 1
            else:
                zero += 1

            max_score = max(max_score, zero - one)

        if s[-1] == "1":
            one += 1
        # Add total_one
        return max_score + one
