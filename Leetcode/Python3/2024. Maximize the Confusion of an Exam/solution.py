# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/

class Solution:  # Sliding window
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.findMax(answerKey, k, "F"), self.findMax(answerKey, k, "T"))

    def findMax(self, answerKey: str, k: int, changeKey: str):
        maxCount = 0
        left, curK = 0, k
        for right, val in enumerate(answerKey):
            if val == changeKey:
                curK -= 1
            # If use all change chance move left index to next changeKey
            while curK < 0:
                if answerKey[left] == changeKey:
                    curK += 1
                left += 1
            maxCount = max(maxCount, right - left + 1)
        return maxCount
