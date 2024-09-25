// https://leetcode.com/problems/swap-nodes-in-pairs/description/

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

function swapPairs(head: ListNode | null): ListNode | null {
  const root = new ListNode(0, head);
  let prev = root;

  while (head && head.next) {
    const nextNode = head.next;

    prev.next = nextNode;
    head.next = nextNode.next;
    nextNode.next = head;
    prev = head;
    head = head.next;
  }

  return root.next;
}
