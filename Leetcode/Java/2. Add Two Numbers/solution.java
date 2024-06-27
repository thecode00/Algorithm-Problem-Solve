// https://leetcode.com/problems/add-two-numbers/description/

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
class Solution {    // Full adder
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode root = new ListNode(-1);
        ListNode cur = root;

        while (l1 != null || l2 != null || carry != 0){
            int total = carry;

            if (l1 != null){
                total += l1.val;
                l1 =l1.next;
            }

            if (l2 != null){
                total += l2.val;
                l2 = l2.next;
            }

            carry = (int)(total / 10);
            cur.next = new ListNode(total % 10);
            cur = cur.next;
        }

        return root.next;
    }
}