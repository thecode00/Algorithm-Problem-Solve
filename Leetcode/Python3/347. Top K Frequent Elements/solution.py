# https://leetcode.com/problems/top-k-frequent-elements/


from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums).most_common(k)
        # print(list(zip(*count)))[0] Asterisk(*) = unpack zip
        return list(zip(*count))[0]
