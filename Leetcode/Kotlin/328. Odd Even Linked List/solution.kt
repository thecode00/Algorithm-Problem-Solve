// https://leetcode.com/problems/odd-even-linked-list/submissions/

/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

//  TODO: fix null check
class Solution {
    fun oddEvenList(head: ListNode?): ListNode? {
        if (head == null){
            return null;
        }

        val evenHead = head.next
        var even = evenHead
        var odd = head

        while (even?.next != null){
            odd?.next = odd?.next?.next
            even?.next = even?.next?.next

            even = even?.next
            odd = odd?.next
        }

        odd?.next = evenHead

        return head
    }
}