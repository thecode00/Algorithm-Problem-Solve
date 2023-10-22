# https://leetcode.com/problems/word-break/description/
# Ref: https://leetcode.com/problems/word-break/solutions/43808/simple-dp-solution-in-python-with-description/

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for idx in range(len(s)):
            for word in wordDict:
                #  Check end of the string s is word
                if s[idx + 1 - len(word): idx + 1] == word and (idx - len(word) == -1 or dp[idx - len(word)]):
                    dp[idx] = True
        return dp[-1]
