# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        sequence = [0] * (2 * n - 1)
        is_used = [False] * (n + 1)

        self.backtracking(0, sequence, is_used, n)

        return sequence

    def backtracking(self, index: int, seq: List[int], used: List[bool], n: int):
        if index == len(seq):
            return True

        if seq[index] != 0:
            return self.backtracking(index + 1, seq, used, n)

        for cur in range(n, 0, -1):
            if used[cur]:
                continue

            used[cur] = True
            seq[index] = cur

            if cur == 1:
                if self.backtracking(index + 1, seq,  used, n):
                    return True
            elif index + cur < len(seq) and seq[index + cur] == 0:
                seq[index + cur] = cur
                if self.backtracking(index + 1, seq,  used, n):
                    return True
                seq[index + cur] = 0

            used[cur] = False
            seq[index] = 0

        return False
