// https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function deleteDuplicates(head: ListNode | null): ListNode | null {
  if (head === null) {
    return head;
  }

  let cur = head;
  while (cur && cur.next) {
    // Skip same value node
    if (cur.val === cur.next.val) {
      cur.next = cur.next.next;
    } else {
      cur = cur.next;
    }
  }

  return head;
}
