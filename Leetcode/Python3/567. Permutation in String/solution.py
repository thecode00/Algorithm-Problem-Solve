# https://leetcode.com/problems/permutation-in-string/

from collections import defaultdict


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
                