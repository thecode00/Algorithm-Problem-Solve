# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # Save with current min number
        if self.stack and self.stack[-1][1] < val:
            self.stack.append([val, self.stack[-1][1]])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return -1

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return -1


class MinStack:  # Use double stack

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.getMin() >= val:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.getMin() == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return float("inf")


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
