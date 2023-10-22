# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/middle-of-the-linked-list/discuss/1651600/PythonJavaC%2B%2B-Simple-Solution-oror-One-Pass-oror-Beginner-Friendly-oror-Detailed-Explanation
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

            
