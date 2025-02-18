# https://leetcode.com/problems/construct-smallest-number-from-di-string/description

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack: List[int] = []
        result: List[int] = []
        number = 1

        for p in pattern:
            stack.append(number)
            number += 1

            if p == "I":
                result.extend(stack[::-1])
                stack.clear()

        stack.append(number)
        result.extend(stack[::-1])

        return "".join(map(str, result))
