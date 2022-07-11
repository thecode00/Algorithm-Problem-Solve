# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from bisect import bisect_right


class Solution:
    # Using bisect library, Runtime: 249 ms(Very slow)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ords = [ord(s) for s in letters]
        idx = bisect_right(ords, ord(target))
        print(idx)
        return letters[idx] if idx != len(letters) else letters[0]
    # Using custom binary search, Runtime: 117 ms

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0] > target or letters[-1] <= target:  # Exclude out of list range value
            return letters[0]
        start, end = 0, len(letters)
        while start < end:
            mid = start + (end - start) // 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid
        return letters[start]
