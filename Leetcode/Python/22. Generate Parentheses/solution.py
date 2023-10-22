# https://leetcode.com/problems/generate-parentheses/


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(left: int, right: int, parenthesis: str):
            if left == right == n:  # Add result complete parenthesis
                result.append(parenthesis)
                return
            if left < n:    # Add left parenthesis
                generate(left + 1, right, parenthesis + "(")
            # If number of right parenthesis > left parenthesis is invaild parenthesis so add right parenthesis when right < left
            if right < left:    
                generate(left, right + 1, parenthesis + ")")
        generate(0, 0, "")
        return result

