# https://leetcode.com/problems/find-unique-binary-string/description

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        exist = set([int(binary, 2) for binary in nums])
        upper_bound = 2 ** len(nums[0])

        for num in range(upper_bound):
            if num not in exist:
                return format(num, "b").zfill(len(nums[0]))

        return "-1"


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        exist = set([int(num, 2) for num in nums])

        # Make all possible binary string
        binarys = self.makeAllBinary(len(nums[0]))

        for binary in binarys:
            if int(binary, 2) not in exist:
                return binary

        return "-1"

    def makeAllBinary(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]

        result = []
        r = self.makeAllBinary(n - 1)

        for n in r:
            result.append(n + "0")
            result.append(n + "1")

        return result
