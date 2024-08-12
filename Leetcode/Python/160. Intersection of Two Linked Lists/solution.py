# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Runtime: 155 ms
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
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


class Solution:  # Not use extra memory
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA, tempB = headA, headB
        lenA = lenB = 0
        while tempA and tempA.next:
            tempA = tempA.next
            lenA += 1

        while tempB and tempB.next:
            tempB = tempB.next
            lenB += 1

        if tempA != tempB:
            return None

        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        else:
            for _ in range(lenB - lenA):
                headB = headB.next

        while headA:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None
