# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_dict = {}
        node = head
        pos = -1
        while node and node.next:
            pos += 1
            if node in node_dict:
                return node
            print(node)
            node_dict[node] = pos
            node = node.next
    
        
        