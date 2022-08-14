# https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        print(self.size)
        if index >= self.size or self.head == None:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
            
    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        node = Node(val)
        if index > self.size:
            return
        if index == 0:
            node.next = cur
            self.head = node
        else:
            for _ in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node
        
        # Added 1 element so increase size 1
        self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = cur.next
        else:
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)