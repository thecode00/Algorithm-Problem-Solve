# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description

class Solution:  # Hashmap
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []

        id_dict = defaultdict(int)

        for id, num in nums1:
            id_dict[id] += num

        for id, num in nums2:
            id_dict[id] += num

        for key in sorted(id_dict.keys()):
            result.append((key, id_dict[key]))

        return result


class Solution:  # Two pointer
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []

        id_dict = defaultdict(int)

        for id, num in nums1:
            id_dict[id] += num

        for id, num in nums2:
            id_dict[id] += num

        for key in sorted(id_dict.keys()):
            result.append((key, id_dict[key]))

        return result
