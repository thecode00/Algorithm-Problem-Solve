from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operators:
                right, left = num_stack.pop(), num_stack.pop()
                if token == "+":
                    num_stack.append(left + right)
                elif token == "-":
                    num_stack.append(left - right)
                elif token == "*":
                    num_stack.append(left * right)
                else:
                    # Why not yse "//"?
                    # cause "//" operator return floor number ex. -2 // 3 => -0.66666 => -1
                    # but int() remove decimal ex. -2 // 3 -> -0.66666 => 0
                    num_stack.append(int(left / right))
            else:
                num_stack.append(int(token))
        return num_stack[-1]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            if len(token) > 1 and token[0] == "-":
                num_stack.append(token)
            elif token.isdigit():
                num_stack.append(token)
            else:
                right_num = num_stack.pop()
                num_stack[-1] = str(int(eval(num_stack[-1] + token + right_num)))
        return int(num_stack[-1])
