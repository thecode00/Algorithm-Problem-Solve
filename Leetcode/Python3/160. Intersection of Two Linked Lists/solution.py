# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: 
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:  # Runtime: 155 ms
        a_dict = {}
        # Put all headA nodes in a dictionary for detect intersection
        while headA:
            a_dict[headA] = True
            headA = headA.next
        # Checks intersection all nodes in headB 
        while headB:
            if headB in a_dict:
                return headB
            headB = headB.next
        return None