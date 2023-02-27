# https://leetcode.com/problems/edit-distance/description/
# Ref: https://leetcode.com/problems/edit-distance/solutions/159295/python-solutions-and-intuition/


class Solution:  # Similar knapsack problem
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1, len_word2 = len(word1), len(word2)
        dp = [list(range(len_word2 + 1)) for _ in range(len_word1 + 1)]
        for i in range(len_word1 + 1):
            dp[i][0] = i
        for i in range(1, len_word1 + 1):
            for j in range(1, len_word2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j-1]
                else:
                    """
                    dp[i - 1][j] = delete
                    dp[i][j - 1] = insert
                    dp[i - 1][j - 1] = replace
                    """
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1
        print(dp)
        return dp[len_word1][len_word2]
