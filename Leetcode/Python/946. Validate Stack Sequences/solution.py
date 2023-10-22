# https://leetcode.com/problems/validate-stack-sequences/
# Time complexity: O(N)


class Solution:  # Implement problem
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        for num in pushed:
            stack.append(num)
            while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        return pop_index == len(popped)
