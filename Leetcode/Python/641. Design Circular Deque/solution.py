# https://leetcode.com/problems/design-circular-deque/


class MyCircularDeque:
    def __init__(self, k: int):
        self._deque = [None for _ in range(k)]
        self._size = 0
        self._maxlen = k
        self._front = 0
        self._rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self._deque[self._front] = value
        else:
            self._front = (self._front - 1) % self._maxlen
            self._deque[self._front] = value
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self._deque[self._rear] = value
        else:
            self._rear = (self._rear + 1) % self._maxlen
            self._deque[self._rear] = value
        self._size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self._deque[self._front] = None
        self._front = (self._front + 1) % self._maxlen
        self._size -= 1
        if self.isEmpty():  # When self._size == 1 front, rear pointer dont match after delete
            self._front = self._rear
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self._deque[self._rear] = None
        self._rear = (self._rear - 1) % self._maxlen
        self._size -= 1
        if self.isEmpty():  # When self._size == 1 front, rear pointer dont match after delete
            self._front = self._rear
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self._deque[self._front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self._deque[self._rear]

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._maxlen


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
