# https://leetcode.com/problems/design-hashmap/
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 20000
        self.table = [None for _ in range(self.size)]

    def hash(self, val):
        return val * 31 * 31 % self.size

    def put(self, key: int, value: int) -> None:
        hash = self.hash(key)
        node = ListNode(key, value)
        if not self.table[hash]:    # When index of table dont save any data just add node
            self.table[hash] = node
            return
        n = self.table[hash]
        while n:
            if n.key == key:    # If key already exist change value
                n.value = value
                return
            if n.next == None:
                n.next = node

    def get(self, key: int) -> int:
        hash = self.hash(key)
        if not self.table[hash]:
            return -1
        n = self.table[hash]
        while n:
            if n.key == key:
                return n.value
            n = n.next
        return -1   # When there is no saved value
        
    def remove(self, key: int) -> None:
        hash = self.hash(key)
        if not self.table[hash]:
            return
        n = self.table[hash]
        if n.key == key:    # When first node delete
            self.table[hash] = n.next
            return

        pre = None
        while n:
            if n.key == key:
                pre.next = n.next
                return
            pre, n = n, n.next
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)