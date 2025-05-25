# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/description

# Time complexity: O(n ^ 2 * L)
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = [1] * len(words)
        prev = list(range(len(words)))
        length = len(words)

        max_length = 1
        max_index = 0

        for i in range(length):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    if dp[i] < dp[j] + 1 and self.getHamming(words[i], words[j]) == 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j

                        if max_length < dp[i]:
                            max_index = i
                            max_length = dp[i]

        result = []

        while prev[max_index] != max_index:
            result.append(words[max_index])
            max_index = prev[max_index]

        result.append(words[max_index])
        result.reverse()

        return result

    def getHamming(self, word1: str, word2: str) -> int:
        diff = 0

        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff += 1

        return diff
