# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power_set = set()

        power = 0
        while 3 ** power <= n:
            power_set.add(3 ** power)
            power += 1

        power_values = list(power_set)
        power_values.sort()

        for idx in range(len(power_values) - 1, -1, -1):
            if power_values[idx] <= n:
                n -= power_values[idx]
                power_set.remove(power_values[idx])

        return n == 0
