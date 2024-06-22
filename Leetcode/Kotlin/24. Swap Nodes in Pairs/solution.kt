// https://leetcode.com/problems/swap-nodes-in-pairs/description/

/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun swapPairs(head: ListNode?): ListNode? {
        val root = ListNode(-1)
        root.next = head
        var prev = root
        var cur = head

        while (cur?.next != null){
            var nextNode = cur.next
            cur.next = nextNode.next
            nextNode.next = cur
            prev.next = nextNode

            prev = cur
            cur = cur.next
        }

        return root.next
    }
}