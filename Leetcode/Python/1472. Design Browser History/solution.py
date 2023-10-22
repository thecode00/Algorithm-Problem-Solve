# https://leetcode.com/problems/design-browser-history/


class BrowserHistory:

    def __init__(self, homepage: str):
        self.page_stack = [homepage]
        self.size = 1
        self.page_index = 0

    def visit(self, url: str) -> None:
        while self.size - 1 > self.page_index:  # Clear all forward history
            self.size -= 1
            self.page_stack.pop()
        # Add page
        self.page_stack.append(url)
        self.page_index += 1
        self.size += 1

    def back(self, steps: int) -> str:
        while self.page_index and steps:
            steps -= 1
            self.page_index -= 1

        return self.page_stack[self.page_index]

    def forward(self, steps: int) -> str:
        while self.page_index < self.size - 1 and steps:
            steps -= 1
            self.page_index += 1

        return self.page_stack[self.page_index]

        # Your BrowserHistory object will be instantiated and called as such:
        # obj = BrowserHistory(homepage)
        # obj.visit(url)
        # param_2 = obj.back(steps)
        # param_3 = obj.forward(steps)


class BrowserHistory:   # Optimized code

    def __init__(self, homepage: str):
        self.page_stack = [homepage]
        self.end = 0
        self.cur = 0

    def visit(self, url: str) -> None:
        while self.end != self.cur:
            self.page_stack.pop()
            self.end -= 1
        self.end += 1
        self.cur += 1
        self.page_stack.append(url)

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.page_stack[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(len(self.page_stack) - 1, self.cur + steps)
        return self.page_stack[self.cur]
