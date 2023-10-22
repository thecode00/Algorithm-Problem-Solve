# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        count = 0
        for idx in range(k):    # First window
            if s[idx] in vowels:
                count += 1
        max_count = count
        for idx in range(k, len(s)):    # Slide window
            if s[idx - k] in vowels:
                count -= 1
            if s[idx] in vowels:
                count += 1
            max_count = max(count, max_count)
        return max_count
