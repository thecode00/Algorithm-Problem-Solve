# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        if not digits:  # Filter blank string
            return answer

        def dfs(idx, string):
            if len(digits) == len(string):
                answer.append(string)
                return
            for s in num_dict[digits[idx]]:
                dfs(idx + 1, string + s)

        num_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        dfs(0, "")
        return answer
