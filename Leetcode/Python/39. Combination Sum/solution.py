# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        """
        sum() function is time complexity: O(N) it slows down when the numbers size increases
        So stores the sum value in the total argument
        """
        def dfs(total: int, numbers: int, index: int):
            for idx in range(index, len(candidates)):
                numbers.append(candidates[idx])
                total += candidates[idx]
                if total == target:  # Find sum target
                    answer.append(numbers[:])
                elif total > target:    # Can`t make target use backtracking
                    pass
                else:
                    dfs(total, numbers, idx)

                numbers.pop()
                total -= candidates[idx]

        dfs(0, [], 0)
        return answer
