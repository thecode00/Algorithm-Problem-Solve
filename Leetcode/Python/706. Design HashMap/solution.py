# https://leetcode.com/problems/design-hashmap/

class ListNode:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    # Use seperate chaining hash
    def __init__(self):
        self.salt = 2999
        self.table = [None] * 2999

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.salt

        # When index of table dont save any data just add node
        if not self.table[hash_key]:
            self.table[hash_key] = ListNode(key, value)
            return

        # Hash collsion!
        cur = self.table[hash_key]

        while cur:
            # If key already exist change value
            if cur.key == key:
                cur.value = value
                return

            if not cur.next:
                break

            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.salt
        if not self.table[hash_key]:
            return -1

        cur = self.table[hash_key]

        while cur:
            if cur.key == key:
                return cur.value

            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        hash_key = key % self.salt
        if self.table[hash_key]:
            cur = self.table[hash_key]
            if cur.key == key:
                self.table[hash_key] = cur.next
                return

            prev = None

            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    return
                prev = cur
                cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
