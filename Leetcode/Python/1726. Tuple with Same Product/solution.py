# https://leetcode.com/problems/tuple-with-same-product/description

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product_count[nums[i] * nums[j]] += 1

        answer = 0
        for val in product_count.values():
            answer += ((val - 1) * val) // 2
        # one unique (a, b, c, d) makes 8 tuple
        return answer * 8
