# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = ""
        while head.next:
            print(head.val)
            answer += str(head.val)
            head = head.next
        answer += str(head.val) # Check Last element
        return int(answer, 10)