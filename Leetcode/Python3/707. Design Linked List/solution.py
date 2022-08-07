# https://leetcode.com/problems/design-linked-list/

# TODO: try solve
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        # Added a head, so increased the size by 1
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.next = val

    def addAtIndex(self, index: int, val: int) -> None:
        

    def deleteAtIndex(self, index: int) -> None:
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)