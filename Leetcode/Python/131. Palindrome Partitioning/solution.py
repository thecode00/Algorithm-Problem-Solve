# https://leetcode.com/problems/palindrome-partitioning/


class Solution:

    @staticmethod
    def is_pail(s1: str) -> bool:
        return s1 == s1[::-1]

    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def search(sl, path):
            if not sl:
                # If not copy path answer save blank list
                answer.append(path[:])
                return

            for idx in range(1, len(sl) + 1):
                if self.is_pail(sl[:idx]):  # Backtracking
                    path.append(sl[:idx])
                    search(sl[idx:], path)
                    path.pop()  # After search pop
        search(s, [])
        return answer
