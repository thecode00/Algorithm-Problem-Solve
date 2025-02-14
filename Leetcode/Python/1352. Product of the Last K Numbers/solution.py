# https://leetcode.com/problems/product-of-the-last-k-numbers/description

class ProductOfNumbers:  # Time complexity: O(N)
    def __init__(self):
        self.cache = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.__init__()
        else:
            self.size += 1
            self.cache.append(self.cache[-1] * num)

    def getProduct(self, k: int) -> int:
        # We can assume that always the current list has at least k numbers
        # when add 0 we clear cache, so k > self.size is search product 0
        if k > self.size:
            return 0
        else:
            return self.cache[-1] // self.cache[-(k + 1)]


class ProductOfNumbers:  # Time complexity: O(N ^ 2)
    def __init__(self):
        self.arr = []
        self.cache = []

    def add(self, num: int) -> None:
        self.arr.append(num)

    def getProduct(self, k: int) -> int:
        if len(self.arr) == len(self.cache):
            return self.cache[-k]

        for _ in range(len(self.arr) - len(self.cache)):
            self.cache.append(0)

        mul = 1
        for idx in range(len(self.arr) - 1, -1, -1):
            mul *= self.arr[idx]
            self.cache[idx] = mul

        return self.cache[-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
