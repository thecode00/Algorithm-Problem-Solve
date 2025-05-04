# https://leetcode.com/problems/push-dominoes/description

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        length = len(dominoes)
        left = [0] * length
        right = [0] * length
        
        force = 0
        for idx in range(length):
            if dominoes[idx] == "R":
                force = length
            elif dominoes[idx] == "L":
                force = 0
            else:
                force = max(force - 1, 0)

            right[idx] = force
        
        force = 0
        for idx in range(length - 1, -1, -1):
            if dominoes[idx] == "R":
                force = 0
            elif dominoes[idx] == "L":
                force = length
            else:
                force = max(force - 1, 0)

            left[idx] = force
        
        result = [0] * length
        for idx in range(length):
            if left[idx] == right[idx]:
                result[idx] = "."
            elif left[idx] < right[idx]:
                result[idx] = "R"
            else:
                result[idx] = "L"
        
        return "".join(result)