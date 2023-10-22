# https://leetcode.com/problems/lru-cache/
# Ref: https://leetcode.com/problems/lru-cache/solutions/45926/python-dict-double-linkedlist/

from typing import Optional


class DoubleLinkNode:
    def __init__(self, key: int, value: int, prev: Optional["DoubleLinkNode"] = None, next:
                 Optional["DoubleLinkNode"] = None) -> None:
        self.prev = prev
        self.next = next
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Dummy head, tail node
        self.head, self.tail = DoubleLinkNode(0, 0), DoubleLinkNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key].value
            # Refresh LRU cache
            self.put(key, value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:   # Delete from LRU cache
            self.remove_node(self.cache[key])

        if len(self.cache) == self.capacity:
            self.remove_node(self.head.next)

        prev = self.tail.prev
        # Add node previous of self.tail node
        node = DoubleLinkNode(key, value, prev, self.tail)
        prev.next = node
        self.tail.prev = node
        self.cache[key] = node

    def remove_node(self, node: DoubleLinkNode) -> None:
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        self.cache.pop(node.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
