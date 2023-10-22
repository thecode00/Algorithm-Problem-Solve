# https://leetcode.com/problems/design-circular-queue/


from collections import deque


class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:  # Move rear pointer
        if self.queue[self.rear] != None:
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.maxlen
        return True

    def deQueue(self) -> bool:  # Move front pointer
        if self.queue[self.front] == None:
            return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.maxlen
        return True

    def Front(self) -> int:
        if self.queue[self.front] == None:
            return -1
        return self.queue[self.front]

    """
    Rear pointer moved after enqueue()
    So last element index = rear - 1
    """

    def Rear(self) -> int:
        if self.queue[self.rear - 1] == None:
            return -1
        return self.queue[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is not None


class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = deque(maxlen=k)
        self.maxlen = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) >= self.maxlen:
            return False
        self.queue.append(value)
        return True

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True
        return False

    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.maxlen


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
