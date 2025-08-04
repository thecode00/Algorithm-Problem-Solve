# https://leetcode.com/problems/fruit-into-baskets/


from collections import defaultdict


class Solution: # Sliding window
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        max_length = 0
        left = 0

        for right, fruit in enumerate(fruits):
            basket[fruit] += 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length