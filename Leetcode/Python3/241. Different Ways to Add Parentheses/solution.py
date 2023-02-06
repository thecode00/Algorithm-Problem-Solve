# https://leetcode.com/problems/different-ways-to-add-parentheses/


from curses.ascii import isdigit


class Solution:  # Optimized
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        result = []
        for idx, val in enumerate(expression):
            if val in "-*+":
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])

                for l in left:
                    for r in right:
                        if val == "*":
                            result.append(l * r)
                        elif val == "+":
                            result.append(l + r)
                        else:
                            result.append(l - r)
        return result


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        result = []

        for idx in range(len(expression)):
            if not isdigit(expression[idx]):
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(
                    expression[idx + 1:])    # Exclude operator

                for num_l in left:
                    for num_r in right:
                        result.append(
                            eval(str(num_l) + expression[idx] + str(num_r)))

        return result
