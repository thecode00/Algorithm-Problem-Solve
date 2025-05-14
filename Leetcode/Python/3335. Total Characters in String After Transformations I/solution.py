# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description

# Rotating queue, 330 ms
from collections import deque


MOD = 10 ** 9 + 7
A_CODE = ord('a')
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        queue = deque([0] * 26)

        # Character counter
        for char in s:
            code = ord(char) - A_CODE
            queue[code] += 1
        
        # Transform 'z' character
        for _ in range(t):
            count = queue.pop() % MOD

            queue.appendleft(count)
            queue[1] = (queue[1] + count) % MOD

        return sum(queue) % MOD


# Implement, 2300 ms
MOD = 10 ** 9 + 7
A_CODE = ord('a')

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        count = [0] * 26

        for c in s:
            count[ord(c) - A_CODE] += 1

        for _ in range(t):
            newCount = [0] * 26
            for i in range(25):
                newCount[i + 1] = count[i]
            newCount[0] = count[25]
            newCount[1] = (newCount[1] + count[25]) % MOD
            count = newCount

        return sum(count) % MOD
    