// https://leetcode.com/problems/reverse-linked-list-ii/description/

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

function reverseBetween(
  head: ListNode | null,
  left: number,
  right: number
): ListNode | null {
  const root = new ListNode(0, head);
  let start = root;

  for (let i = 0; i < left - 1; i++) {
    start = start.next;
  }
  const end = start.next;

  for (let i = 0; i < right - left; i++) {
    const nextNode = start.next;

    start.next = end.next;
    end.next = end.next.next;
    start.next.next = nextNode;
  }

  return root.next;
}
