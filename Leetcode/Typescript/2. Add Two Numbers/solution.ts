// https://leetcode.com/problems/add-two-numbers/description/

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

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  const root = new ListNode();
  let cur = root,
    carry = 0;

  while (l1 || l2 || carry) {
    let total = carry;

    if (l1) {
      total += l1.val;
      l1 = l1.next;
    }
    if (l2) {
      total += l2.val;
      l2 = l2.next;
    }

    cur.next = new ListNode(total % 10);
    cur = cur.next;
    carry = total >= 10 ? 1 : 0;
  }

  return root.next;
}
