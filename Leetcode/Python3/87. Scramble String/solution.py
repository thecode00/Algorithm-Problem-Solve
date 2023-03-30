# https://leetcode.com/problems/scramble-string/
# Ref: https://leetcode.com/problems/scramble-string/solutions/3357546/python3-35ms-beats-99-38-recursion-with-memoization/


from collections import Counter, defaultdict
from functools import lru_cache


class Solution:
    def __init__(self):
        self.dp = {}

    @lru_cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.dp:  # Search from cache dict
            return self.dp[(s1, s2)]

        if Counter(s1) != Counter(s2):
            return False

        if len(s1) <= 2:
            return True

        func = self.isScramble
        for idx in range(1, len(s1)):
            if (func(s1[idx:], s2[idx:]) and (func(s1[:idx], s2[:idx]))) or (func(s1[idx:], s2[:-idx]) and (func(s1[:idx], s2[-idx:]))):
                self.dp[(s1, s2)] = True    # Tuple is immutable so tuple can use dict key
                return True
        self.dp[(s1, s2)] = False   # Not answer
        return False


class Solution:  # Use nested function
    def isScramble(self, s1: str, s2: str) -> bool:
        dp = defaultdict(bool)

        def search(s1: str, s2: str) -> bool:
            if (s1, s2) in dp:  # Search from cache dict
                return dp[(s1, s2)]
            if Counter(s1) != Counter(s2):
                return False
            if len(s1) < 3:
                return True

            for idx in range(1, len(s1)):
                if (search(s1[:idx], s2[-idx:]) and search(s1[idx:], s2[:-idx])) or (search(s1[:idx], s2[:idx]) and search(s1[idx:], s2[idx:])):
                    dp[(s1, s2)] = True  # Tuple is immutable so tuple can use dict key
                    return True
            dp[(s1, s2)] = False  # Not answer
            return False
        return search(s1, s2)
