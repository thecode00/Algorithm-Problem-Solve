# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

# Runner
class Solution:
    def isPalindrome(self, head):
        rev = None  # Reversed liked list
        slow = fast = head
        while fast and fast.next:   # Find mid element
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:    # If fast != None linked list size is odd so exclude mid element
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = deque()
        
        if not head:
            return True
        
        while head:
            queue.append(head.val)
            head = head.next
        
        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False
        return True

        