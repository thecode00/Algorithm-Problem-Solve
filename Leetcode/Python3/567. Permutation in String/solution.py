# https://leetcode.com/problems/permutation-in-string/

from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = Counter(s1)
        cur_count = Counter()

        left = right = 0
        for right in range(len(s2)):
            cur_count[s2[right]] += 1

            if cur_count == c1:
                return True
            
            if right >= len(s1) - 1:    # If len(window) == len(s1) move left index of window
                cur_count[s2[left]] -= 1
                left += 1
                # If you add an empty counter, elements with a value of 0 disappear.
                cur_count += Counter()
        return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        string = defaultdict(int)
        for s in s1:
            string[s] += 1
        answer = False
        for idx in range(len2 - len1 + 1):
            temp = defaultdict(int)
            for s in s2[idx: idx + len1]:
                temp[s] += 1
            if temp == string:
                answer = True
            if answer:
                return answer
        return answer
                