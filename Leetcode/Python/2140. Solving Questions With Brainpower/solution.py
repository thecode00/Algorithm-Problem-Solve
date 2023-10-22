# https://leetcode.com/problems/solving-questions-with-brainpower/
# Ref: https://leetcode.com/problems/solving-questions-with-brainpower/solutions/1694329/recursion-dp-fully-explained-with-amazing-visualization-c/?orderBy=most_votes


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        # Add a zero to the end for ease of calculation
        dp = [0] * (length + 1)
        for idx in range(length - 1, -1, -1):
            point, power = questions[idx]
            # Compare not select current problem and select problem
            dp[idx] = max(
                dp[idx + 1], dp[min(idx + power + 1, length)] + point)
        return dp[0]
