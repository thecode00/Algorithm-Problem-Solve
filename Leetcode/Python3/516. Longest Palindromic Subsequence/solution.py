# https://leetcode.com/problems/longest-palindromic-subsequence/description/
# Ref: https://leetcode.com/problems/longest-palindromic-subsequence/solutions/1468396/c-python-2-solutions-top-down-dp-bottom-up-dp-o-n-space-clean-concise/


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[left][right] = s[left: right + 1] longest palindrome
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for left in range(len(s) - 1, -1, -1):
            dp[left][left] = 1
            for right in range(left + 1, len(s)):
                # When s = "bcb", left = 0, right = 2, dp[left][right] = dp[left + 1][right - 1] + 2 = "b" + 'c' + "b"
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] + 2
                else:   # When s = "abc", left = 0, right = 0, "a" != "c" so compare "ab", "bc"
                    dp[left][right] = max(
                        dp[left + 1][right], dp[left][right - 1])
        return dp[0][len(s) - 1]
