# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:  # Runtime: 58 ms
        l1, l2 = len(word1), len(word2)
        min_length = min(l1, l2)
        answer = ""
        for idx in range(min_length):
            answer += word1[idx] + word2[idx]
        if l1 == l2:
            return answer
        else:
            if l1 > l2:
                for idx in range(l1 - l2):
                    answer += word1[idx + l2]
            else:
                for idx in range(l2 - l1):
                    answer += word2[idx + l1]
            return answer

    def mergeAlternately(self, word1: str, word2: str) -> str:  # Runtime: 34 ms
        l1, l2 = len(word1), len(word2)
        answer = ""
        for s1, s2 in zip(word1, word2):
            answer += s1 + s2
        if l1 == l2:
            return answer
        else:
            if l1 > l2:
                for idx in range(l1 - l2):
                    answer += word1[idx + l2]
            else:
                for idx in range(l2 - l1):
                    answer += word2[idx + l1]
            return answer
