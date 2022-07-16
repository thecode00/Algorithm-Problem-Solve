# https://leetcode.com/problems/find-the-difference/

from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_t = defaultdict(int)
        for string in t:
            dict_t[string] += 1
        for string in s:
            dict_t[string] -= 1
        # print(dict_t)

        for key in dict_t.keys():
            if dict_t[key] != 0:
                return key
