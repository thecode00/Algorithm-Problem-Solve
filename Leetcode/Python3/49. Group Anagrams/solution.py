"""
https://leetcode.com/problems/group-anagrams/
Time Complexity: O()
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for s in strs:
            str_dict[tuple(sorted(s))].append(s)
        return list(str_dict.values())
