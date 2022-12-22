"""
https://leetcode.com/problems/group-anagrams/
Time Complexity: O()
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for s in strs:
            # sorted() return sorted list so use join() replace list to string
            str_dict["".join(sorted(s))].append(s)
        return list(str_dict.values())
