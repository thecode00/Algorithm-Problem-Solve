# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []

        idx = 0
        while idx < len(words):
            result.append(words[idx])

            # Skip same group
            while idx < len(words) - 1 and groups[idx] == groups[idx + 1]:
                idx += 1
            idx += 1

        return result
