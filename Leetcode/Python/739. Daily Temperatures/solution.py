# https://leetcode.com/problems/daily-temperatures/


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                past = stack.pop()  # (idx, temp)
                answer[past[0]] = idx - past[0]
            stack.append((idx, temp))
        return answer
