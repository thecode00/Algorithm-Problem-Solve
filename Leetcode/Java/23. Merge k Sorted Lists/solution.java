// https://leetcode.com/problems/merge-k-sorted-lists/submissions/1296204625/

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
    // After inserting the nodes into the priority queue, retrieve the node with the minimum value and connect it to the root node
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> priorityQ = new PriorityQueue<>((n1, n2) -> {
            if (n1.val == n2.val){
                return 0;
            } else if (n1.val > n2.val){
                return 1;
            } else {
                return -1;
            }
        });

        for (ListNode node : lists){
            if (node != null){
                priorityQ.add(node);
            }
        }

        ListNode root = new ListNode(-1);
        ListNode cur = root;

        while (!priorityQ.isEmpty()){
            ListNode node = priorityQ.poll();
            cur.next = node;
            cur = cur.next;

            if (node.next != null){
                priorityQ.add(node.next);
            }
        }

        return root.next;


    }
}