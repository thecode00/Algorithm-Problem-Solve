# https://leetcode.com/problems/finding-3-digit-even-numbers/description

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter = Counter(digits)
        result = []

        for target in range(100, 1000, 2):
            first = target // 100
            second = (target // 10) % 10
            third = target % 10

            # Use digits to form the target number
            counter[first] -= 1
            counter[second] -= 1
            counter[third] -= 1

            if counter[first] >= 0 and counter[second] >= 0 and counter[third] >= 0:
                result.append(target)
                    
            counter[first] += 1
            counter[second] += 1
            counter[third] += 1
    
        return result