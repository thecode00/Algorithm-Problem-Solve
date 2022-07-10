# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from bisect import bisect_right


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ords = [ord(s) for s in letters]
        idx = bisect_right(ords, ord(target))
        return letters[idx]
