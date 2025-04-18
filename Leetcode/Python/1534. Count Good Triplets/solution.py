# https://leetcode.com/problems/count-good-triplets/description

# Bruteforce
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0

        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, len(arr)):
                        if (self.isGoodTriplet(i, j, k, b, c, arr)):
                            count += 1
        return count

    def isGoodTriplet(self, i: int, j: int, k: int, b: int, c: int, arr: List[int]) -> bool:
        return abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c