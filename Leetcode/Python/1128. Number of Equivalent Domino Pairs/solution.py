# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = defaultdict(int)
        pairs = 0

        for a, b in dominoes:
            key1 = f"{a}{b}"
            key2 = f"{b}{a}"

            pairs += counter[key1]
            
            # Prevent duplicate
            if a != b:
                pairs += counter[key2]
            
            counter[key1] += 1
        
        return pairs