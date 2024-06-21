// https://leetcode.com/problems/merge-two-sorted-lists/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null){
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        
        // Always set the smaller one as list1
        if (list1.val > list2.val){
            ListNode smallNode = list2;
            list2 = list1;
            list1 = smallNode;
        }
            
        list1.next = this.mergeTwoLists(list1.next, list2);
        
        return list1;
    }
}