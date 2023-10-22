# https://leetcode.com/problems/contains-duplicate/

from collections import Counter


class Solution:  # Runtime: 866ms
    def containsDuplicate(self, nums: List[int]) -> bool:
        # most_common returns a tuple list consisting of (element, number of elements) in descending order of the number of elements.
        count = Counter(nums).most_common()
        # print(count)
        return True if count[0][1] != 1 else False
