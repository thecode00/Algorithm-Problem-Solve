# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        union = set()
        result = []

        for idx, (num_a, num_b) in enumerate(zip(A, B)):
            union.add(num_a)
            union.add(num_b)
            # 2 * (idx + 1) = amount of prefix array element
            # intersection count = amount of prefix array element - len(union)
            result.append(2 * (idx + 1) - len(union))

        return result
