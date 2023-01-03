# https://leetcode.com/problems/detect-capital/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # istitle(): if first letter is uppercase and rest is lowercase return True
        return word.isupper() or word.islower() or word.istitle()
