# https://leetcode.com/problems/linked-list-random-node/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
from random import random


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.root = head
        self.length = 0
        while head:
            self.length += 1
            head = head.next

    def getRandom(self) -> int:
        r = math.floor(random() * self.length)
        temp_node = self.root
        while r > 0:
            temp_node = temp_node.next
            r -= 1
        return temp_node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
