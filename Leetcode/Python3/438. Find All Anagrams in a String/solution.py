"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
Time complexity: O(N ^ 2)
"""


from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram = Counter()
        count_p = Counter(p)
        result = []

        left = 0
        for right in range(len(s)):
            anagram[s[right]] += 1

            if anagram == count_p:
                result.append(left)

            if right >= len(p) - 1:
                anagram[s[left]] -= 1
                # Add an empty counter to remove elements below zero.
                anagram += Counter()
                left += 1
        return result
