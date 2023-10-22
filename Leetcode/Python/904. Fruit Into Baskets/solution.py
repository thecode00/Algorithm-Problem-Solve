# https://leetcode.com/problems/fruit-into-baskets/


from collections import defaultdict


class Solution: # Sliding window
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)

        max_fruits = 0
        count = defaultdict(int)
        left = right = 0
        for right in range(len(fruits)):
            count[fruits[right]] += 1

            if len(count) <= 2:
                max_fruits = max(max_fruits, sum(count.values()))
            else:   
                while len(count) > 2:
                    count[fruits[left]] -= 1
                    if count[fruits[left]] == 0:
                        del count[fruits[left]]
                    left += 1
        return max_fruits
                