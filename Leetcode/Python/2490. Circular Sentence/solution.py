# https://leetcode.com/problems/circular-sentence/description

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        for idx in range(len(words) - 1):
            if words[idx][-1] != words[idx + 1][0]:
                return False

        return words[0][0] == words[-1][-1]
