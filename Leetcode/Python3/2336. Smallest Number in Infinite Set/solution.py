# https://leetcode.com/problems/smallest-number-in-infinite-set/description/


class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set()    # Save popped numbers set
        self.smallest = 1

    def popSmallest(self) -> int:
        return_num = self.smallest
        self.removed.add(self.smallest)
        while self.smallest in self.removed:    # Find next smallest number
            self.smallest += 1
        return return_num

    def addBack(self, num: int) -> None:
        if num in self.removed:  # If num was popped add num to infinite set
            self.smallest = min(self.smallest, num)
            self.removed.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
