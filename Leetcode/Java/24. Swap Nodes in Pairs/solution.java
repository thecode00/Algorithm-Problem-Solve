// https://leetcode.com/problems/swap-nodes-in-pairs/description/

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
    public ListNode swapPairs(ListNode head) {
        ListNode prev = new ListNode(-1, head);
        ListNode root = prev;

        while (head != null && head.next != null){
            ListNode nextNode = head.next;
            prev.next = nextNode;
            head.next = nextNode.next;
            nextNode.next = head;

            prev = head;
            head = head.next;
        }

        return root.next;
    }
}