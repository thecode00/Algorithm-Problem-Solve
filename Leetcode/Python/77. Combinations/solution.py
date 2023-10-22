# https://leetcode.com/problems/combinations/


from itertools import combinations

# Use itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, combinations(range(1, n + 1), k)))


# DFS
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        numbers = list(range(1, n + 1))
        def dfs(index: int, result: List[int]) -> None:
            if len(result) == k:
                answer.append(result[:])
                return
            for idx in range(index, n):
                print(idx, index)
                result.append(numbers[idx])
                dfs(idx + 1, result)
                result.pop()
        dfs(0, [])
        return answer
            